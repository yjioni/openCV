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

plt.style.use('fivethirtyeight')

plt.subplot(131)
hist = cv2.calcHist([img], [0,1], None, [50,50], [0,256,0,256])
p = plt.imshow(hist)
plt.title('blue and green')
plt.colorbar(p)

plt.subplot(132)
hist = cv2.calcHist([img], [1,2], None, [50,50], [0,256,0,256])
p = plt.imshow(hist)
plt.title('green and red')
plt.colorbar(p)

plt.subplot(133)
hist = cv2.calcHist([img], [0,2], None, [50,50], [0,256,0,256])
p = plt.imshow(hist)
plt.title('blue and red')
plt.colorbar(p)


cv2.imshow('img', img)

plt.show()


cv2.waitKey()
cv2.destroyAllWindows()
