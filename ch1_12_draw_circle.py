import cv2
import numpy as np

from tkinter import *
from tkinter import filedialog

root = Tk()
root.filename = filedialog.askopenfilename(
                    title= 'select an image for a background',
                    initialdir= 'C:/Users/',
                    filetypes= (('jpg files', '*.jpg'), ('all files', '*.*'))
                    )
img = cv2.imread(root.filename)

# 원
cv2.circle(img, (150, 150), 100, (200, 0, 10))
cv2.circle(img, (400, 150), 30, (110, 100, 20), -1, cv2.LINE_AA)

# 타원, 반원
cv2.ellipse(img, (50, 300), (50, 50), 0, 0, 360, (0, 0, 255))
cv2.ellipse(img, (150, 300), (30, 50), 0, 0, 360, (0, 0, 255))
cv2.ellipse(img, (150, 300), (30, 50), 0, 180, 360, (0, 200, 0), -1)
cv2.ellipse(img, (400, 425), (50, 75), 45, 180, 360, (100, 200, 0))
cv2.ellipse(img, (400, 425), (50, 75), 0, 180, 360, (100, 200, 250))
cv2.ellipse(img, (350, 425), (50, 80), 300, 0, 180, (100, 200, 0))

# 원 안에 별
cv2.circle(img, (250, 250), 100, (100, 300, 100), -1, cv2.LINE_AA)
star = np.array([[335, 200], [155, 270], [328, 310], [200, 165], [230, 350]], dtype=np.int32)
cv2.polylines(img, [star], True, (0, 250, 250), 5)

cv2.imshow('circle', img)
cv2.waitKey()
cv2.destroyAllWindows()