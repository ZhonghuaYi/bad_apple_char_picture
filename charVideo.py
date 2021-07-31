import cv2 as cv
import numpy as np
from PIL import Image, ImageDraw, ImageFont

video_path = "F:\\Viedos\\bad_apple.mp4"
font_path = "C:\\Windows\\Fonts\\seguibl.ttf"
font_size = 30
pixel_density = 3/5
resize_var = 1 / (font_size*pixel_density)

(r, g, b, a) = (0, 0, 0, 225)

cap = cv.VideoCapture(video_path)
fps = int(cap.get(cv.CAP_PROP_FPS))
print(fps)

video_w = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
video_h = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
print(video_w, video_h)
fourcc = cv.VideoWriter_fourcc('X', 'V', 'I', 'D')
writer = cv.VideoWriter('out.avi', fourcc, fps, (video_w, video_h), False)

count = 0
while cap.isOpened():
    count += 1
    ret, frame = cap.read()
    # 如果正确读取，ret为True
    if not ret:
        print("Video reading error.")
        break

    # 将彩色转为灰色，再转为二值
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    retval, dst = cv.threshold(gray, 128, 255, cv.THRESH_BINARY)
    height, width = dst.shape

    # 帧缩放
    new_frame = cv.resize(dst, (int(width * resize_var), int(height * resize_var)), interpolation=cv.INTER_CUBIC)
    new_height, new_width = new_frame.shape

    # 使用PIL设置画布
    draw_font = ImageFont.truetype(font_path, font_size)
    draw_img = Image.new("L", (new_width * font_size, new_height * font_size), 256)
    draw = ImageDraw.Draw(draw_img)
    for i in range(new_height):
        for j in range(new_width):
            if new_frame[i, j] != 0:
                draw.text((3/5*j * font_size, 3/5*i * font_size), '#', font=draw_font)

    # 写入视频文件
    writer.write(np.array(draw_img))

    if count == 600:
        print(new_frame)
        break

    # cv.imshow('frame', np.array(draw_img))
    # if cv.waitKey(1) == ord('q'):
    #     print(new_width, new_height)
    #     break

cap.release()
writer.release()
print(1)
cv.destroyAllWindows()

if __name__ == '__main__':

