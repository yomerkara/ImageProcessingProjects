import cv2
import numpy as np

img1 = cv2.imread('image1.png')
img2 = cv2.imread('image2.png')

# sum = cv2.add(img1, img2)
weighted = cv2.addWeighted(img1, 0.7, img2, 0.3,0)
cv2.imshow('sum', weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
