from setting import picture_settings as picset

import cv2 as cv
import numpy as np
from PIL import Image, ImageDraw, ImageFont


class Char2Picture:

    def __init__(self, pic_path, font_path, font_size, pixel_density):
        self.__pic_path = pic_path
        self.__font_path = font_path
        self.__font_size = int(font_size)
        self.__pixel_density = pixel_density
        self.img_binary = None
        self.ret = None

    def transform(self):
        # read picture, 0 means read as gray picture.
        img = cv.imread(self.__pic_path, 0)
        # transform gray picture into binary.
        img_binary = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, 0)
        self.img_binary = img_binary
        self.ret = None

    def char_image_draw(self, char_set):
        char_set = list(char_set)
        resize_pic = cv.resize(self.img_binary, None, fx=1/self.__font_size, fy=1/self.__font_size, \
                               interpolation=cv.INTER_AREA)
        size = resize_pic.shape
        random_char = np.random.choice(char_set, size=size)

        draw_font = ImageFont.truetype(self.__font_path, self.__font_size)
        draw_img = Image.new("L", self.img_binary.shape, 256)
        draw = ImageDraw.Draw(draw_img)

        for i in range(size[0]):
            for j in range(size[1]):
                if resize_pic[i, j]:
                    random_char[i, j] = ' '
            text = ''.join(random_char[i])
            print(i)
            draw.text((0, i * self.__font_size), text, font=draw_font)
        cv.imshow('1', np.array(draw_img))

    def binary_picture_save(self, save_path):
        cv.imwrite(save_path, self.img_binary)


if __name__ == '__main__':
    char_pic = Char2Picture(picset['picture_path'], picset['font_path'], picset['font_size'], picset['pixel_density'])
    char_pic.transform()
    char_pic.char_image_draw(picset['char_set'])
    cv.waitKey(0)
    # cv.imshow('picture', char_pic.img_binary)
    # if cv.waitKey(1000) == ord('s'):
    #     char_pic.binary_picture_save(picset['save_path'])
