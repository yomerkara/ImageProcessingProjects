import cv2
from matplotlib import pyplot as plt
import numpy as np

image = cv2.imread('saat.png')

image[80, 80] = [0, 255, 255]

rectangle = image[75:150, 75:150]
image[0:75, 0:75] = rectangle
# image[75:150, 75:150] = [255, 255, 0]
cv2.rectangle(image, (75, 75), (150, 150), (0, 255, 0), 2)
cv2.imshow('clock', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
