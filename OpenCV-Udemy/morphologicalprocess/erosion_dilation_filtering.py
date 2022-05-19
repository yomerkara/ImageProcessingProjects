import cv2
import numpy as np
from matplotlib import pyplot as plt

j = cv2.imread('j.png')
j1 = cv2.imread('j2.png')
j2 = cv2.imread('j3.png')

kernel = np.ones((2, 2), np.uint8) / 255

erosion = cv2.erode(j1, kernel, iterations=1)
dilation = cv2.dilate(j2, kernel, iterations=1)

plt.subplot(321), plt.imshow(j), plt.title('org'), plt.xticks([]), plt.yticks([])
plt.subplot(322), plt.imshow(j), plt.title('org'), plt.xticks([]), plt.yticks([])
plt.subplot(323), plt.imshow(j1), plt.title('j1'), plt.xticks([]), plt.yticks([])
plt.subplot(324), plt.imshow(erosion), plt.title('erosion'), plt.xticks([]), plt.yticks([])
plt.subplot(325), plt.imshow(j2), plt.title('j2'), plt.xticks([]), plt.yticks([])
plt.subplot(326), plt.imshow(dilation), plt.title('dilation'), plt.xticks([]), plt.yticks([])

plt.show()
