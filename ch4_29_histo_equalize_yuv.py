import cv2
import numpy as np
import matplotlib.pylab as plt

from tkinter import *
from tkinter import filedialog

root = Tk()
root.filename = filedialog.askopenfilename(title='select an image',
                                    initialdir='C:/Users/',
                                    filetypes=(('jpg files', '*.jpg'),
                                               ('all files', '*.*'))
                                            )

img = cv2.imread(root.filename)
# cv2.equalizeHist(대상) >> 8bit 1channel 만 지원
# img3 = cv2.equalizeHist(img) >> error

img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

img2 = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)


cv2.imshow('before', img)
cv2.imshow('after', img2)

cv2.waitKey()
cv2.destroyAllWindows()
