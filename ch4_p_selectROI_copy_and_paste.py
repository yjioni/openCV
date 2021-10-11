import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog

def select_roi():
    global img
    x, y, w, h = cv2.selectROI('img', img, False)
    cv2.rectangle(img, (x-1, y-1), (x+w, y+h), (255,255,0), 1)
    cv2.imshow('img', img)
    
    if w and h:
        roi = img[y:y+h, x:x+w]
        x1, y1 = cv2.selectROI('img', img, False)[0:2]
        img[y1:y1+h, x1:x1+w] = roi
        cv2.imshow('img', img)

root = Tk()
root.filename = filedialog.askopenfilename(
                    title= 'select an image for a background',
                    initialdir= 'C:/Users/',
                    filetypes= (('jpg files', '*.jpg'), 
                                ('png files', '*.png'), 
                                ('all files', '*.*')
                                )
                    )
img = cv2.imread(root.filename)
cv2.imshow('img', img)
select_roi()
cv2.waitKey()
cv2.destroyAllWindows()
