import cv2
import numpy as np

# 빈 화면 만들기 
# img = np.full((500, 500, 3), 255, dtype=np.uint8)
# cv2.imwtite('../blank_500.jpg', img)

img = cv2.imread('C:/Users/oing9/Documents/Crawling/img/blank_500.jpg')

cv2.line(img, (50, 50), (150, 50), (255, 0, 0))
cv2.line(img, (50, 100), (150, 100), (0, 155, 0))
cv2.line(img, (50, 150), (150, 150), (0, 0, 255))

# line_thickness = 10
cv2.line(img, (100, 200), (400, 200), (155, 200, 110), 10)
cv2.line(img, (100, 250), (400, 250), (250, 150, 250), 10)
cv2.line(img, (100, 300), (400, 300), (0, 250, 250), 10)
cv2.line(img, (100, 350), (400, 350), (200, 200, 200), 10)
cv2.line(img, (100, 400), (400, 400), (0, 0, 0), 10)

cv2.line(img, (100, 450), (400, 250), (0, 0, 255), 20, cv2.LINE_4)
cv2.line(img, (100, 400), (400, 200), (0, 0, 255), 20, cv2.LINE_8)
cv2.line(img, (100, 350), (400, 150), (0, 0, 255), 20, cv2.LINE_AA)

cv2.line(img, (500, 0), (0, 500), (0, 0, 0), 1, cv2.LINE_AA)

cv2.imshow('lines', img)
cv2.waitKey()
cv2.destroyAllWindows()