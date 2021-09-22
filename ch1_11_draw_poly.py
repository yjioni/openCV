import cv2
import numpy as np
from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename = filedialog.askopenfilename(
    initialdir='C:/Users/',
    title='open file',
    filetype=(('jpg files', '*.jpg'), ('all files', '*.*'))
)

img = cv2.imread(root.filename)
# 번개모양
pts1 = np.array([[50, 50], [150, 150], [50, 140], [200, 240]], dtype=np.int32)
cv2.polylines(img, [pts1], True, (255,0,0), 5)

# 삼각형
pts2 = np.array([[350, 150], [200, 150], [300, 100]], dtype=np.int32)
cv2.polylines(img, [pts2], True, (0, 0, 0), 3)

# 꼭지점
pts3 = np.array([[150, 300], [50, 450], [250, 450]], dtype=np.int32)
cv2.polylines(img, [pts3], False, (150, 0, 200), 4)

# 5각형
pts4 = np.array([[350, 250], [450, 350], [400, 450],
[300, 450], [250, 350]], dtype=np.int32)
cv2.polylines(img, [pts4], True, (100, 200, 100), 3)

# 별모양
pts5 = np.array([[350,250], [400, 450], [250, 350], [450, 350], [300, 450]], dtype=np.int32)
cv2.polylines(img, [pts5], True, (130, 100, 30), 3)

cv2.imshow('rectangle', img)
cv2.waitKey()
cv2.destroyAllWindows()

