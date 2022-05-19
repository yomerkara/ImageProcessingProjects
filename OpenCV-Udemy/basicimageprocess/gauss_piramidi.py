import cv2

img = cv2.imread('cicekJPG.jpg')
cv2.imshow('org', img)

up = cv2.pyrUp(img)
cv2.imshow('up', up)  # çözünürlük * 2

down = cv2.pyrDown(img)  # çözünürlük /2
cv2.imshow('down', down)

cv2.waitKey(0)
cv2.destroyAllWindows()
