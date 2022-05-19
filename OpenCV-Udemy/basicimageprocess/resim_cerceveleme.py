import cv2
import numpy as np
from matplotlib import pyplot as plt

blue = [255, 0, 0]

image = cv2.imread('opencvdark.png')
scale_percent = 30  # percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)

image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

replicate = cv2.copyMakeBorder(image, 10, 10, 10, 10,
                               cv2.BORDER_REPLICATE)  # It replicates the last element. Suppose, if image contains letters “abcdefgh” then output will be “aaaaa|abcdefgh|hhhhh“.
reflect = cv2.copyMakeBorder(image, 10, 10, 10, 10,
                             cv2.BORDER_REFLECT)  # The border will be mirror reflection of the border elements. Suppose, if image contains letters “abcdefg” then output will be “gfedcba|abcdefg|gfedcba“.
reflect101 = cv2.copyMakeBorder(image, 10, 10, 10, 10,
                                cv2.BORDER_REFLECT101)  # It does the same works as cv2.BORDER_REFLECT but with slight change. Suppose, if image contains letters “abcdefgh” then output will be “gfedcb|abcdefgh|gfedcba“.
wrap = cv2.copyMakeBorder(image, 10, 10, 10, 10,
                          cv2.BORDER_WRAP)  # this reflects the pixel from the opposite boundary as cdefgh|abcdefgh|abcdefg
constant = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT,
                              value=blue)  # It adds a constant colored border. The value should be given as a keyword argument
"""cv2.imshow('org', image)
cv2.imshow('replicate', replicate)
cv2.imshow('reflect', reflect)
cv2.imshow('reflect101', reflect101)
cv2.imshow('wrap', wrap)
cv2.imshow('constant', constant)"""

plt.subplot(231), plt.imshow(image, 'gray'), plt.title('org')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('replicate')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('reflect')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('reflect101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('wrap')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('constant')

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
