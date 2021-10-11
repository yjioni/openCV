import cv2
import numpy as np

img = cv2.imread('./img/sunset.jpg')

x, y, w, h = cv2.selectROI('img', img, False)
if w and h:
    roi = img[y:y+h, x:x+w]
    cv2.imshow('cropped', roi)
    cv2.moveWindow('cropped', 0,0)
    cv2.imwrite('C:/Users/oing9/Documents/Crawling/cropped.jpg', roi)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
