import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog

isDragging = False
x0, y0, w, h = -1, -1, -1, -1
blue, red = (255,0,0), (0,0,255)
roi2 = 0
paste_x, paste_y = 0, 0

def onMouse(event, x, y, flags, param):
    global isDragging, x0, y0, img, roi2, paste_x, paste_y, w, h
    if event == cv2.EVENT_LBUTTONDOWN:
        isDragging = True
        x0 = x
        y0 = y
    elif event == cv2.EVENT_MOUSEMOVE:
        if isDragging:
            img_draw = img.copy()
            cv2.rectangle(img_draw, (x0,y0), (x,y), blue, 2)
            cv2.imshow('img', img_draw)
    elif event == cv2.EVENT_LBUTTONUP:
        isDragging = False
        w = x-x0
        h = y-y0
        print('x:{}, y:{}, w:{}, h:{}'.format(x0, y0, w, h))
        if w > 0 and h > 0:
            img_draw = img.copy()
            cv2.rectangle(img_draw, (x0,y0), (x0+w,y0+h), red, 2)
            cv2.imshow('img', img_draw)
            roi = img[y0:y0+h, x0:x0+w]
            roi2 = roi
        elif w < 0 and h < 0:
            img_draw = img.copy()
            print('>> w: {},  h: {}, x0: {}, y0: {}'.format(w, h, x0, y0) )
            cv2.rectangle(img_draw,(x0+w, y0+h), (x0,y0),  red, 2)
            cv2.imshow('img', img_draw)
            roi = img[y0+h:y0, x0+w:x0]
            roi2 = roi
        else:
            cv2.imshow('img', img)
            print('영역을 드래그 하세요.')
    elif event == cv2.EVENT_RBUTTONDOWN:
        print('x:{}, y:{}에 붙여넣습니다.'.format(x, y))
        isDragging=True

    elif event == cv2.EVENT_RBUTTONUP:
        isDragging=False
        img[y:y+h, x:x+w] = roi2
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
cv2.setMouseCallback('img', onMouse)
cv2.waitKey()
cv2.destroyAllWindows()
