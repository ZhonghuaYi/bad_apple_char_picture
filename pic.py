import cv2 as cv
from PIL import Image, ImageDraw, ImageFont
import cv2
img = cv2.imread('D:\\OneDrive\\Pictures\\headimage\\20200504_130926785_iOS.jpg')
font = cv2.FONT_HERSHEY_SIMPLEX

imgzi = cv2.putText(img, '000', (50, 300), font, 1.2, (0, 255, 255), 2)

cv2.imshow('',imgzi)
cv2.waitKey(0)
cv2.destroyAllWindows()