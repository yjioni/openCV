import cv2
import numpy as np

win_name = 'Track bar'
img = cv2.imread('C:/Users/oing9/Documents/Crawling/img/blank_500.jpg')
cv2.imshow(win_name, img)

color = tuple()

def onChange(x):
    global color
    print(x)
    b = cv2.getTrackbarPos('B', win_name)
    g = cv2.getTrackbarPos('G', win_name)
    r = cv2.getTrackbarPos('R', win_name)
    print(r, g, b)
    color = (b, g, r)
    return color

cv2.createTrackbar('R', win_name, 255, 255, onChange)
cv2.createTrackbar('G', win_name, 255, 255, onChange)
cv2.createTrackbar('B', win_name, 255, 255, onChange)

def onMouse(event, x, y, flags, param):
    global color
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 10, color, -1)
        cv2.imshow(win_name, img)
cv2.setMouseCallback(win_name, onMouse)        

while True:
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()

