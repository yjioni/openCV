import cv2
import numpy as np

img = cv2.imread('C:/Users/oing9/Documents/Crawling/img/sunset.jpg')
x = 320
y = 150
w = 50
h = 50

roi = img[y:y+h, x:x+w]

print(roi.shape)
cv2.rectangle(roi, (0,0), (h-1, w-1), (0,0,255))
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()