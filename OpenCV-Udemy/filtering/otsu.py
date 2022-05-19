import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gurultuluresim.JPG', 0)

_, basicThreshold = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, otsuThreshold2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

blur = cv2.GaussianBlur(img, (5, 5), 0)
_, otsuBlurThreshold2 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

imgs = [img, 0, basicThreshold,
        img, 0, otsuThreshold2,
        blur, 0, otsuBlurThreshold2]

titles = ['OrgGurultulu', 'Histogram', 'Basit Thresholding',
          'OrgGurultulu', 'Histogram', 'Otsu Thresholding',
          'Gaussian Blur', 'Histogram', 'Blured Otsu Thresholding']

for i in range(3):
    plt.subplot(3, 3, i * 3 + 1), plt.imshow(imgs[i * 3], 'gray')
    plt.title(titles[i * 3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i * 3 + 2), plt.hist(img[i * 3].ravel(), 256)
    plt.title(titles[i * 3 + 1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i * 3 + 3), plt.imshow(imgs[i * 3 + 2], 'gray')
    plt.title(titles[i * 3 + 2]), plt.xticks([]), plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
