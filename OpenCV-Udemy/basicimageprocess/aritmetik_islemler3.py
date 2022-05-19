import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('image.png')
img2 = cv2.imread('opencvdark.png')

scale = 30
width = int(img2.shape[1] * (scale / 100))
height = int(img2.shape[0] * (scale / 100))

dim = (width, height)
img2 = cv2.resize(img2, dim, interpolation=cv2.INTER_AREA)

print(img2.shape)  # (1024, 831, 3) row,column,channel
row, column, channel = img2.shape
roi = img1[0:row, 0:column]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)  # image2'yi gri tona çevirdik.
# cv2.imshow('img2gray', img2gray)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)  # 10-255 eşik değerleri arasını alıyoruz.
print(ret)
# cv2.imshow('mask', mask)
mask_reverse = cv2.bitwise_not(mask)
# cv2.imshow('mask_reverse', mask_reverse)

img1background = cv2.bitwise_and(roi, roi, mask=mask_reverse)
# cv2.imshow('img1background', img1background)

img2foreground = cv2.bitwise_and(img2, img2, mask=mask)
# cv2.imshow('img2foreground', img2foreground)

end = cv2.add(img1background, img2foreground)
# cv2.imshow('end', end)

img1[0:row, 0:column] = end
# cv2.imshow('endAdd', img1)

plt.subplot(241), plt.imshow(img2gray, 'gray'), plt.title('img2gray')
plt.subplot(242), plt.imshow(mask, 'gray'), plt.title('mask')
plt.subplot(243), plt.imshow(mask_reverse, 'gray'), plt.title('mask_reverse')
plt.subplot(244), plt.imshow(img1background, 'gray'), plt.title('img1background')
plt.subplot(245), plt.imshow(img2foreground, 'gray'), plt.title('img2foreground')
plt.subplot(246), plt.imshow(end, 'gray'), plt.title('end')
plt.subplot(247), plt.imshow(img1, 'gray'), plt.title('endAdd')

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
