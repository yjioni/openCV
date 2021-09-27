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
cv2.imshow('img', img)

# 히스토그램 계산
channels = cv2.split(img)
print(channels)
colors = ('b', 'g', 'r')

for (ch, color) in zip(channels, colors):
    hist = cv2.calcHist([ch], [0], None, [256], [0, 256])
    plt.plot(hist, color=color)
plt.show()
