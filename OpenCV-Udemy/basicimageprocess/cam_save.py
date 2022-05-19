import cv2

cam = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # hangi formatta kaydedilsin

save = cv2.VideoWriter('save.avi', fourcc, 20.0, (640, 480))  # 20.0 = saniye kaç görüntü, 4. parametre video boyutu

while (cam.isOpened()):
    ret, frame = cam.read()
    if ret == True:
        frame = cv2.flip(frame, 0)
        save.write(frame)
        cv2.imshow('save', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

cam.release()
save.release()
cv2.destroyAllWindows()
