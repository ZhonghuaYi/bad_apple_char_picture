from setting import picture_settings as picset
import tool

import cv2 as cv
import numpy as np


class CharPicture:

    def __init__(self, pic_path, font_path, font_size, pixel_density):
        self.__pic_path = pic_path
        self.__font_path = font_path
        self.__font_size = int(font_size)
        self.__pixel_density = pixel_density
        self.origin_img = cv.imread(pic_path)
        self.img_binary = None
        self.ret = None
        self.char_image = None

    def transform_binary(self):
        # read picture, 0 means read as gray picture.
        img = cv.cvtColor(self.origin_img, cv.COLOR_BGR2GRAY)
        # transform gray picture into binary.
        img_binary = tool.gray_to_binary(img)
        self.img_binary = img_binary
        self.ret = None

    def char_image_draw(self, char_set):
        new_image = tool.binary_to_char(char_set, self.img_binary, self.__font_size)
        self.char_image = new_image

    def binary_picture_save(self, save_path):
        cv.imwrite(save_path, self.img_binary)

    def char_picture_save(self, save_path):
        cv.imwrite(save_path, self.char_image)


if __name__ == '__main__':
    char_pic = CharPicture(picset['picture_path'], picset['font_path'], picset['font_size'], picset['pixel_density'])
    char_pic.transform_binary()
    char_pic.char_image_draw(picset['char_set'])
    cv.imshow('binary picture', char_pic.img_binary)
    cv.imshow('char picture', char_pic.char_image)
    if cv.waitKey(1000) == ord('s'):
        char_pic.char_picture_save(picset['save_path'])
