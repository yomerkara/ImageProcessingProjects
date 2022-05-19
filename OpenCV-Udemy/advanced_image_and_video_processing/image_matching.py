import cv2
import numpy as np
import matplotlib.pyplot as plt
# !!! Buraya tekrar bak!!!

searching_image = cv2.imread('kucuk_resim.JPG', 0)
img = cv2.imread('buyuk_resim.JPG', 0)

orb = cv2.ORB_create()  # küçülmüş veya döndürülmüş resimleri bulmada kullanılır.
key1, target1 = orb.detectAndCompute(searching_image, None)
key2, target2 = orb.detectAndCompute(img, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
match = bf.match(target1, target2)
match = sorted(match, key=lambda x: x.distance)
end_img = cv2.drawMatches(searching_image, key1, img, key2, match[0:10], None, flags=2)

plt.imshow(end_img)
plt.show()
