import cv2 as cv
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# path = "D:\\OneDrive\Pictures\\acg\\MJK_17_T622_006.png"
# img = cv.imread(path)
# cv.imshow('image', img)
# print(type(img))
# cv.waitKey(0)

font_path = "C:\\Windows\\Fonts\\times.ttf"
font_size = 12

height, width = 144,256
draw_font = ImageFont.truetype(font_path, font_size)
draw_img = Image.new("L", (width*font_size, height*font_size), 256)
draw = ImageDraw.Draw(draw_img)
start = 0
for i in range(height):
    for j in range(width):
        draw.text((j*font_size, i*font_size), '#', font=draw_font)
arr = np.array(draw_img)
print(type(arr))