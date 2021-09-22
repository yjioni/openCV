import cv2
from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename = filedialog.askopenfilename(
    initialdir='C:/Users/',
    title='open file',
    filetype=(('jpg files', '*.jpg'), ('all files', '*.*'))
)

img = cv2.imread(root.filename)

cv2.rectangle(img, (50, 50), (100, 150), (255, 0, 0))
cv2.rectangle(img, (200, 50), (400, 100), (0, 255, 0), 10)
cv2.rectangle(img, (400, 200), (200, 450), (0, 0, 255), -1)

cv2.imshow('rectangle', img)
cv2.waitKey()
cv2.destroyAllWindows()

