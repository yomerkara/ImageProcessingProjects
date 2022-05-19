import cv2
import numpy as np


def write_text():
    white_space = np.zeros((640, 720, 3), np.uint8)
    white_space.fill(255)

    font_scale = 1.0
    color = (0, 0, 255)
    font_face = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(white_space, 'FONT_HERSHEY_COMPLEX', (25, 40), font_face, font_scale, color)
    font_face = cv2.FONT_HERSHEY_COMPLEX_SMALL
    cv2.putText(white_space, 'FONT_HERSHEY_COMPLEX_SMALL', (25, 80), font_face, font_scale, color)
    font_face = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(white_space, 'FONT_HERSHEY_DUPLEX', (25, 120), font_face, font_scale, color)
    font_face = cv2.FONT_HERSHEY_PLAIN
    cv2.putText(white_space, 'FONT_HERSHEY_PLAIN', (25, 160), font_face, font_scale, color)
    font_face = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    cv2.putText(white_space, 'FONT_HERSHEY_SCRIPT_COMPLEX', (25, 200), font_face, font_scale, color)
    font_face = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    cv2.putText(white_space, 'FONT_HERSHEY_SCRIPT_SIMPLEX', (25, 240), font_face, font_scale, color)
    font_face = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(white_space, 'FONT_HERSHEY_SIMPLEX', (25, 280), font_face, font_scale, color)
    font_face = cv2.FONT_HERSHEY_TRIPLEX
    cv2.putText(white_space, 'FONT_HERSHEY_TRIPLEX', (25, 320), font_face, font_scale, color)
    font_face = cv2.FONT_ITALIC
    cv2.putText(white_space, 'FONT_ITALIC', (25, 320), font_face, font_scale, color)

    img = cv2.imread('cicek.png')
    cv2.imshow('cicek', img)

    rectangle = cv2.rectangle(img, (200, 70), (320, 180), (0, 255, 0), 2)
    cv2.imshow('cerceve', rectangle)

    img = np.zeros((400, 400, 3), dtype='uint8')
    dortgen = cv2.rectangle(img, (10, 10), (390, 210), (0, 0, 255), 2)
    line = cv2.line(img, (10, 10), (390, 210), (0, 255, 251), 2)
    circle = cv2.circle(img, (200, 200), 100, (255, 0, 251), 2)
    cv2.putText(img, 'Omer Kara', (5, 300), cv2.FONT_ITALIC, 2, (255, 255, 255), 4, cv2.LINE_4)
    cv2.imshow('line', line)

    cv2.namedWindow('text ornekler')
    cv2.imshow('text ornekler', white_space)
    cv2.imwrite('text_ornekler.jpg', white_space)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    write_text()


if __name__ == "__main__":
    main()
