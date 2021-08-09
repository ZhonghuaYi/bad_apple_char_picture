from setting import video_settings as videoset
import tool

import cv2 as cv
import numpy as np


class CharVideo:

    def __init__(self, video_path, font_path, font_size, pixel_density):
        self.__video_path = video_path
        self.__font_path = font_path
        self.__font_size = font_size
        self.__pixel_density = pixel_density
        self.__origin_video = cv.VideoCapture(video_path)
        self.__origin_width = int(self.__origin_video.get(cv.CAP_PROP_FRAME_WIDTH))
        self.__origin_height = int(self.__origin_video.get(cv.CAP_PROP_FRAME_HEIGHT))
        self.__origin_fps = self.__origin_video.get(cv.CAP_PROP_FPS)
        self.__origin_size = (self.__origin_width, self.__origin_height)

    def transform(self, save_path, char_set, trans_type):
        video_fourcc = cv.VideoWriter_fourcc('m', 'p', '4', 'v')
        video_writter = cv.VideoWriter(save_path, video_fourcc, self.__origin_fps, self.__origin_size)
        origin_video = self.__origin_video
        # process video
        while origin_video.isOpened():
            success, frame = origin_video.read()
            if not success:
                break
            else:
                gray_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                binary_img = tool.gray_to_binary(gray_img)
                if trans_type == 'binary':
                    img_color = tool.binary_to_color(binary_img)
                    cv.imshow('img', img_color)
                    video_writter.write(img_color)
                elif trans_type == 'char':
                    img_color = tool.binary_to_char(char_set, binary_img, self.__font_size)
                    cv.imshow('img', img_color)
                    video_writter.write(img_color)
                if cv.waitKey(1) == ord('q'):
                    break
        origin_video.release()
        video_writter.release()
        cv.destroyAllWindows()


if __name__ == '__main__':
    char_video = CharVideo(videoset['video_path'], videoset['font_path'], videoset['font_size'], videoset['pixel_density'])
    char_video.transform(videoset['save_path'], videoset['char_set'], 'char')
