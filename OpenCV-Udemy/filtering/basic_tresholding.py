import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gradient.JPG')

_, threshold1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, threshold2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, threshold3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, threshold4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, threshold5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['ORG', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
imgs = [img, threshold1, threshold2, threshold3, threshold4, threshold5]

for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(imgs[i], 'gray'), plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
