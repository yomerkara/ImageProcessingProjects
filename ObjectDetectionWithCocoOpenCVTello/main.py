import cv2
import keyPressModule as kp
from djitellopy import tello
import cvzone
import time

# cap = cv2.VideoCapture(0)  # bu kısım drone kullanılırken silinecek.
# cap.set(3, 640)  # set width #bu kısım drone kullanılırken silinecek.
# cap.set(4, 480)  # set height #bu kısım drone kullanılırken silinecek.
thres = 0.6
nmsThres = 0.2

classNames = []
classFile = 'coco.names'

with open(classFile, 'rt') as f:
    classNames = f.read().split('\n')
print(classNames)
configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = "frozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

kp.init()
me = tello.Tello()
me.connect()
#me.send_rc_control(0, 0, 0, 0)
print(me.get_battery())
me.streamoff()
me.streamon()

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    if kp.getKey("LEFT"):
        lr = -speed
    elif kp.getKey("RIGHT"):
        lr = speed
    if kp.getKey("UP"):
        fb = speed
    elif kp.getKey("DOWN"):
        fb = -speed
    if kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed
    if kp.getKey("a"):
        yv = speed
    elif kp.getKey("d"):
        yv = -speed

    if kp.getKey("q"): me.land();time.sleep(3)
    if kp.getKey("e"): me.takeoff()

    if kp.getKey("z"):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
        time.sleep(0.3)

    return [lr, fb, ud, yv]


while True:
    vals = getKeyboardInput()
    img = me.get_frame_read().frame
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    # success, img = cap.read()
    classIds, confs, bbox = net.detect(img, confThreshold=thres,
                                       nmsThreshold=nmsThres)  # nmsThresh'i eğer multiple same object detectliyeceksen kaldır veya düşür.
    try:
        for classId, conf, box in zip(classIds.flatten(), confs.flatten(), bbox):
            # print(classId, box, conf)
            cv2.putText(img, f'{classNames[classId - 1].upper()} {round(conf * 100, 2)}',
                        (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)
            cvzone.cornerRect(img, box, rt=0)

    except:
        pass

    #me.send_rc_control(0, 0, 0, 0)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
