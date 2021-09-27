# 4-25 cv2.calcHist()
# cv2.calcHist()  스케일 이미지의 히스토그램 계산하여 그림
# 해당 그림은 gray color 1차원 그래프 작성

import cv2
import numpy as np
import matplotlib.pylab as plt


from tkinter import *
from tkinter import filedialog

root = Tk()
root.filename = filedialog.askopenfilename(
                        title='choose csv file',
                        initialdir='C:/Users/',
                        filetypes=(('jpg files', '*.jpg'),
                                    ('all files', '*.*'))
                        )


img = cv2.imread(root.filename, cv2.IMREAD_GRAYSCALE)

cv2.imshow('img', img)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)
plt.show()
print(hist.shape)

# 히스토그램 총 합계, 이미지 크기
print(hist.sum(), img.shape)
