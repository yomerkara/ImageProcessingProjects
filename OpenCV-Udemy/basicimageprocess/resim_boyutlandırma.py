import cv2

img = cv2.imread('cicek.png')
screen_details = 1280, 720

scale_width = screen_details[0] / img.shape[1]
scale_height = screen_details[1] / img.shape[0]
scale = min(scale_width, scale_height)

screen_width = int(img.shape[1] * scale)
screen_height = int(img.shape[0] * scale)

cv2.namedWindow('Scaleable Screen', cv2.WINDOW_NORMAL) # cv2.WINDOW_NORMAL pencerenin yeniden boyutlandırılabilmesini sağlar.
cv2.resizeWindow('Scaleable Screen', screen_width, screen_height)

cv2.imshow('Scaleable Screen', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
