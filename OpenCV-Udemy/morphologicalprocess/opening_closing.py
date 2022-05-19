import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    _, frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_green = np.array([36, 0, 0])
    upper_green = np.array([86, 255, 255])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    end_frame = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((5, 5), np.float32) / 25

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN,
                               kernel=kernel)  # filtrede uymayan kısımları(gürültü) belirginleştirir.
    cv2.imshow('opening', opening)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel=kernel)  # gürültüyü kapatır.
    cv2.imshow('closing', closing)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
