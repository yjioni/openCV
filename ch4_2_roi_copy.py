import cv2
import numpy as np

img = cv2.imread('C:/Users/oing9/Documents/Crawling/img/sunset.jpg')

x = 320
y = 150
w = 50
h = 50

roi = img[y:y+h, x:x+w]
img2 = roi.copy()

img[y:y+h, x+w:x+w+w] = roi
cv2.rectangle(img, (x+w,y), (x+w+w, y+h), (0,255,0))
cv2.rectangle(img, (x,y), (x+w-1, y+h), (255,0,0))

cv2.imshow('img', img)
cv2.imshow('copy', img2)
cv2.waitKey()
cv2.destroyAllWindows()