import cv2
import numpy as np
from matplotlib import pyplot as plt

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_green = np.array([36, 0, 0])
    upper_green = np.array([86, 255, 255])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    end_frame = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((15, 15), np.float32) / 255
    smoothed = cv2.filter2D(end_frame, -1, kernel)
    blur = cv2.GaussianBlur(end_frame, (15, 15), 0)
    median = cv2.medianBlur(end_frame, 15)
    bilateral = cv2.bilateralFilter(end_frame, 15, 60, 60)

    kernel2 = np.ones((5, 5), np.float32) / 25
    erosion = cv2.erode(end_frame, kernel2, iterations=1)  # gürültüleri silmek için kullanılır.
    cv2.imshow('erosion', erosion)
    dilation = cv2.dilate(end_frame, kernel2, iterations=1)  # gürültüleri arttırmak için kullanılır.
    cv2.imshow('dilation', dilation)

    

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
