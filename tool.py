import cv2 as cv
import numpy as np


def gray_to_binary(gray_img):
    img_binary = cv.adaptiveThreshold(gray_img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, 0)
    blurred = cv.GaussianBlur(img_binary, (11, 11), 0)
    img_binary = cv.Canny(blurred, 1, 250)
    return img_binary


def binary_to_color(img_binary):
    shape = img_binary.shape
    img_color = np.zeros(shape=(shape[0], shape[1], 3), dtype='uint8')
    for i in range(3):
        img_color[:, :, i] = img_binary
    return img_color


def binary_to_char(char_set, img_binary, multiple):
    char_set = list(char_set)
    # resize the picture according to the font size
    resize_pic = cv.resize(img_binary, None, fx=1 / multiple, fy=1 / multiple,
                           interpolation=cv.INTER_AREA)
    size = resize_pic.shape
    # get random characters matrix
    random_char = np.random.choice(char_set, size=size)
    # initialize image which ready for putting text on it
    shape = img_binary.shape
    new_image = np.zeros(shape=(shape[0], shape[1], 3), dtype='uint8')
    # render char image
    for i in range(size[0]):
        for j in range(size[1]):
            if not resize_pic[i, j]:
                random_char[i, j] = ' '
            cv.putText(new_image, random_char[i, j], (j * multiple, i * multiple),
                       cv.FONT_HERSHEY_PLAIN, multiple / 10, (255, 255, 255), 1, lineType=cv.LINE_AA)
    return new_image
