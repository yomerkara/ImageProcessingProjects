import cv2
import numpy as np
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

img_path = ""


def read_text(img_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel = np.ones((1, 1), np.uint8)
    img = cv2.erode(img, kernel, iterations=1)
    img = cv2.dilate(img, kernel, iterations=1)

    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    cv2.imwrite(img_path + 'cleared.png', img)

    if img_path == "a1.png":
        end_img = pytesseract.image_to_string(Image.open(img_path + 'cleared.png'), lang="tur")
    elif img_path == "a2.png":
        end_img = pytesseract.image_to_string(Image.open(img_path + 'cleared.png'), lang="tur")
    else:
        end_img = pytesseract.image_to_string(Image.open(img_path + 'cleared.png'))

    return end_img


print(read_text("a.png"))
print(read_text("a1.png"))
print(read_text("a2.png"))
print(read_text("b.png"))
