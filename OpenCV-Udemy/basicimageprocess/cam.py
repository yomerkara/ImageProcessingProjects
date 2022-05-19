import cv2

cam = cv2.VideoCapture(0)  # kamera sayısına göre numara veriliyor, eğer mp4 dosyası çağırılacaksa path verilir.
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 320)  # width yeniden boyutlandırma
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)  # height yeniden boyutlandırma

while True:
    ret, video = cam.read()
    """ret = cam.set(3, 640)  # 3. bilgi width yeniden boyutlandırma
    ret = cam.set(4, 480)  # 4.bilgi height yeniden boyutlandırma"""
    gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
    cv2.imshow('video', video)
    cv2.imshow('gray', gray)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cam.release()  # görüntüyü bırak
cv2.destroyAllWindows()
