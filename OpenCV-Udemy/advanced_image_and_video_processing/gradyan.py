import cv2
import numpy as np

img = cv2.imread('kose_bulma.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray32 = np.float32(gray)

gradyan32 = cv2.goodFeaturesToTrack(gray32, 100, 0.01, 10)  # köşe tespiti için kullanılıyor.(100 = max nokta sayısı)
# (0.01) = hassasiyet (10 = mesafe)
gradyan = np.int0(gradyan32)

for grad in gradyan:
    x, y = grad.ravel()  # x ve y koordinatlarını aldık.
    cv2.circle(img, (x, y), 3, 255, -1)

cv2.imshow('gradyan', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
