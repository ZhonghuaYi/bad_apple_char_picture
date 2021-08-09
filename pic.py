import numpy as np
import cv2
import tool

img = cv2.imread('D:\\OneDrive\\Pictures\\headimage\\20200504_130926785_iOS.jpg')
font = cv2.FONT_HERSHEY_SIMPLEX

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_binary = tool.gray_to_binary(img_gray)
img_color = tool.binary_to_color(img_binary)

cv2.imshow('', img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()