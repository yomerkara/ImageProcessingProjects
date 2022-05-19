import cv2

cam = cv2.VideoCapture(0)


def res_1080():
    cam.set(3, 1920)
    cam.set(4, 1080)


def res_720():
    cam.set(3, 1280)
    cam.set(4, 720)


def res_480():
    cam.set(3, 640)
    cam.set(4, 480)


def res_out(width, height):
    cam.set(3, width)
    cam.set(4, height)


def scale(frame, percent=75):
    width = int(frame.shape[1] * percent / 100)
    height = int(frame.shape[0] * percent / 100)
    dim = (width, height)

    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)


res_480()

while True:
    ret, frame = cam.read()
    cv2.imshow('frameOrg', frame)
    frame75 = scale(frame)
    cv2.imshow('frame75', frame75)
    frame50 = scale(frame, 50)
    cv2.imshow('frame50', frame50)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
