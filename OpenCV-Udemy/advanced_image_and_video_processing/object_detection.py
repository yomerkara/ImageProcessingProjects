import cv2
import numpy as np

img_rgb = cv2.imread('ana_resim.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

object = cv2.imread('template.jpg', 0)

w, h = object.shape[::-1]  # print(np.shape(object)) = (22, 19)

resources = cv2.matchTemplate(img_gray, object, cv2.TM_CCOEFF_NORMED)  # object detection yöntemi
# matchTemplate değişken olmayan içeriklerde kullanılabilir. image gibi. ışık ve mesafe değişmemeli
# cv2.TM_CCOEFF_NORMED = Template Matching Correlation Coefficient =>
# https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html
threshold = 0.8

loc = np.where(resources > threshold)  # eşleşmenin threshold değerinden büyük olduğu noktaları tutuyor.

for n in zip(*loc[::-1]):
    """
    print(loc)
    paralel iterasyon
    >>> numbers = [1, 2, 3]
    >>> letters = ['a', 'b', 'c']
    >>> zipped = zip(numbers, letters)
    >>> zipped  # Holds an iterator object
    <zip object at 0x7fa4831153c8>
    >>> type(zipped)
    <class 'zip'>
    >>> list(zipped)
[(1, 'a'), (2, 'b'), (3, 'c')]"""
    cv2.rectangle(img_rgb, n, (n[0] + w, n[1] + h), (0, 255, 255), 2)

cv2.imshow('detected', img_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()
