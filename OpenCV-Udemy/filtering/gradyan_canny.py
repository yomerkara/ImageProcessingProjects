import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while (1):
    ret, frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low_white = np.array([0, 0, 140])
    up_white = np.array([256, 60, 256])

    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelX = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobelY = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)

    mask_white = cv2.inRange(hsv, low_white, up_white)
    # cv2.imshow('mask_white', mask_white)
    end_white = cv2.bitwise_and(frame, frame, mask=mask_white)
    # cv2.imshow('end_white', end_white)

    canny = cv2.Canny(frame, 100, 200)

    cv2.imshow('laplacian', laplacian)
    cv2.imshow('sobelX', sobelX)
    cv2.imshow('sobelY', sobelY)
    cv2.imshow('canny', canny)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
