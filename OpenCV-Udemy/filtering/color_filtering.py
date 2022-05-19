import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while (1):
    ret, frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    """ HSV nedir ?
    Hue(renk tonu), Saturation(doygunluk) and Value(değer) renk uzayıdır.
    Ton => rengi, Doygunluk =>griliği, Değer =>parlaklığı temsil eder.
    BGR veya RGB renk uzayına kıyasla daha iyi performans gösterir.
    Hue(renk tonu) aralığı => [0,179]
    Saturation(doygunluk) aralığı => [0,255]
    Value(değer) aralığı => [0,255]'dir.  
    """

    low_red = np.array([150, 30, 30])
    up_red = np.array([190, 255, 255])
    mask_red = cv2.inRange(hsv, low_red, up_red) # hsv'ye dönüştürülmüş framede lower-upper aralığını maske olarak tut.
    # cv2.imshow('mask_red', mask_red)
    end_red = cv2.bitwise_and(frame, frame, mask=mask_red)
    # cv2.imshow('end_red', end_red)

    low_blue = np.array([100, 60, 60])
    up_blue = np.array([140, 255, 255])
    mask_blue = cv2.inRange(hsv, low_blue, up_blue)
    # cv2.imshow('mask_blue', mask_blue)
    end_blue = cv2.bitwise_and(frame, frame, mask=mask_blue)
    # cv2.imshow('end_blue', end_blue)

    low_white = np.array([0, 0, 140])
    up_white = np.array([256, 60, 256])
    mask_white = cv2.inRange(hsv, low_white, up_white)
    # cv2.imshow('mask_white', mask_white)
    end_white = cv2.bitwise_and(frame, frame, mask=mask_white)
    # cv2.imshow('end_white', end_white)

    kernel = np.ones((15, 15), np.float32) / 225
    smoothed = cv2.filter2D(end_white, -1, kernel)
    cv2.imshow('smoothed', smoothed)

    blur = cv2.GaussianBlur(end_white, (15, 15), 0)
    cv2.imshow('blur', blur)

    median = cv2.medianBlur(end_white, 15)
    cv2.imshow('median', median)

    bilateral = cv2.bilateralFilter(end_white, 15, 75, 75)
    cv2.imshow('bilateral', bilateral)

    # cv2.imshow('video', frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
