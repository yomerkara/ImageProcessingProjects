import cv2
import numpy as np
from matplotlib import pyplot as plt

# Buraya tekrar bak!!!

img = cv2.imread('on_plan.jpg')
mask = np.zeros(img.shape[:2], np.uint8)

bgModel = np.zeros((1, 65), np.float64)
fgModel = np.zeros((1, 65), np.float64)

rectangle = (250, 125, 150, 250)

cv2.grabCut(img, mask, rectangle, bgModel, fgModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
img = img * mask2[:, :, np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()
