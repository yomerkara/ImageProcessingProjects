import cv2
import numpy as np


def save(path, image, jpeg_quality=None, png_compress=None):
    if jpeg_quality:
        cv2.imwrite(path, image,
                    [int(cv2.IMWRITE_JPEG_QUALITY), jpeg_quality])  # jpg kalitesi 0-100 arasında 100 max kalite
    elif png_compress:
        cv2.imwrite(path, image, [int(cv2.IMWRITE_PNG_COMPRESSION),
                                  png_compress])  # sıkıştırma 0-9 arasında yüksek değer küçük boyut fazla sıkıştırma demek.
    else:
        cv2.imwrite(path, image)


def main():
    img_path = "cicek.png"
    img = cv2.imread(img_path)

    cv2.imshow('cicek', img)

    jpeg_out = 'cicekJPG.jpg'
    save(jpeg_out, img, jpeg_quality=60)

    out_png = 'cicekPNG.png'
    save(out_png, img, png_compress=9)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
