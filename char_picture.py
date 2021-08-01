from setting import picture_settings as picset

import cv2 as cv
import numpy as np
from PIL import Image, ImageDraw, ImageFont


class Char2Picture:

    def __init__(self, pic_path, font_path, font_size, pixel_density):
        self.origin_img = cv.imread(pic_path, 0)
        self.__pic_path = pic_path
        self.__font_path = font_path
        self.__font_size = int(font_size)
        self.__pixel_density = pixel_density
        self.img_binary = None
        self.ret = None
        self.char_image = None

    def transform(self):
        # read picture, 0 means read as gray picture.
        img = self.origin_img
        # transform gray picture into binary.
        img_binary = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, 0)
        blurred = cv.GaussianBlur(img_binary, (11, 11), 0)
        img_binary = cv.Canny(blurred, 10, 70)
        self.img_binary = img_binary
        self.ret = None

    def char_image_draw(self, char_set):
        # get characters list which required to render
        char_set = list(char_set)
        # resize the picture according to the font size
        resize_pic = cv.resize(self.img_binary, None, fx=1/self.__font_size, fy=1/self.__font_size, \
                               interpolation=cv.INTER_AREA)
        size = resize_pic.shape
        # get random characters matrix
        random_char = np.random.choice(char_set, size=size)
        # initialize image which ready for putting text on it
        new_image = np.zeros(self.origin_img.shape)

        for i in range(size[0]):
            for j in range(size[1]):
                if not resize_pic[i, j]:
                    random_char[i, j] = ' '
                cv.putText(new_image, random_char[i, j], (j*self.__font_size, i*self.__font_size), \
                           cv.FONT_HERSHEY_PLAIN, self.__font_size / 10, (255, 255, 255), 1, lineType=cv.LINE_AA)
        self.char_image = new_image

    def binary_picture_save(self, save_path):
        cv.imwrite(save_path, self.img_binary)

    def char_picture_save(self, save_path):
        cv.imwrite(save_path, self.char_image)


if __name__ == '__main__':
    char_pic = Char2Picture(picset['picture_path'], picset['font_path'], picset['font_size'], picset['pixel_density'])
    char_pic.transform()
    char_pic.char_image_draw(picset['char_set'])
    cv.imshow('picture', char_pic.char_image)
    if cv.waitKey(1000) == ord('s'):
        char_pic.char_picture_save(picset['save_path'])
