import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_white = np.array([0, 0, 140])
    upper_white = np.array([256, 60, 256])

    mask = cv2.inRange(hsv, lower_white, upper_white)
    end_frame = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((15, 15), np.float32) / 255
    blur = cv2.filter2D(end_frame, -1, kernel)
    gaussian_blur = cv2.GaussianBlur(end_frame, (15, 15), 0)
    median = cv2.medianBlur(end_frame, 15)
    bilateral = cv2.bilateralFilter(end_frame, 15, 75, 75)

    cv2.imshow('end_frame', end_frame), cv2.imshow('blur', blur), cv2.imshow('gaussian_blur', gaussian_blur)
    cv2.imshow('median', median), cv2.imshow('bilateral', bilateral)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
