import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sudoku.JPG', 0)
img = cv2.medianBlur(img, 5)

_, threshold = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
adaptiveThresholdMeanC = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2) # ortalama alır
adaptiveThresholdGaussianC = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2) # ağırlıklı ortalama alır

titles = ['ORG', 'Basic 127', 'MEANC', 'GAUSSIANC']
imgs = [img, threshold, adaptiveThresholdMeanC, adaptiveThresholdGaussianC]

for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(imgs[i], 'gray'), plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
