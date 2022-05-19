import cv2
import numpy as np

# image = cv2.imread('image.png', 0)  # image okuma methodu //0 parametresi gri tonlama için kullanılır.
image = cv2.imread('image.png')
# cv2.imshow('PNG', image)  # show methodu
cv2.imwrite('gray.png', image)  # image'ı kaydetme methodu

print(str(image.item(100, 100, 0)))  # (100,100) aralığında //0 mavi, 1 yeşil , 2 kırmızı piksel değerini döndürür
image.itemset((100, 100, 1), 0)  # 100-100 noktasında mavi kırmızı veya yeşil değerini değiştirir.
print(
    str(image.shape))  # eğer resim renkliyse renk parametresi de gelir(3 parametre ),# eğer griyse renk parametresi gelmez(2 parametre)
print(str(len(image.shape)))  # //len methoduyla gri mi renkli mi olduğu anlaşılabilir.(3 mü 2 mi?)
print(
    str(image.size))  # kaç pixel olduğunun bilgisini verir # 3ton olduğu için(kırmızı, mavi, yeşil)pixel size renkli resimlerde gri resimlerin pixel sizeının 3 katıdır.
print(image.dtype)  # veri tipi

ROI = image[210:290, 172:230]  # [y,x] parametrelerin yerlerine dikkat!!
image[210:290, 72:130] = ROI  # pixel eşitleme//roideki pixelleri buraya yapıştır.
b, g, r = cv2.split(image)  # renklere ayrıştırma
cv2.merge((b, g, r))  # ayrıştırılan renkleri tekrar mergeleme

blue = image[:, :, 0]  # renk erişimi bu şekilde de yapılabilir.0=blue,1=green,2=red
image[:, :, 0] = 255
cv2.imshow('cut', image)
cv2.waitKey(0)  # kullanıcı bir tuşa basana kadar bekle
cv2.destroyAllWindow()
