import cv2

img = cv2.imread('sayfa.jpg')

_, th = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY)
_, th1 = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY_INV)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, th2 = cv2.threshold(gray, 12, 255, cv2.THRESH_BINARY)

gauss = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
_, otsu = cv2.threshold(gray, 12, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('org', img)
cv2.imshow('th', th)
cv2.imshow('th1', th1)
cv2.imshow('th2', th2)
cv2.imshow('gauss', gauss)
cv2.imshow('otsu', otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()
