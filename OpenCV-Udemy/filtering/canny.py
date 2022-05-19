import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('image1.png', 0)
canny = cv2.Canny(img, 50, 200)
plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('original'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(canny, cmap='gray'), plt.title('kenarlar'), plt.xticks([]), plt.yticks([])

plt.show()