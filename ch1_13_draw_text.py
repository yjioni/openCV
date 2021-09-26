import cv2

from tkinter import *
from tkinter import filedialog

root = Tk()
root.filename = filedialog.askopenfilename(
                    title= 'select an image for a background',
                    initialdir= 'C:/Users/',
                    filetypes= (('jpg files', '*.jpg'), ('all files', '*.*'))
                    )
img = cv2.imread(root.filename)

cv2.putText(img, 'Plane', (30, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))
cv2.putText(img, 'Simplex', (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
cv2.putText(img, 'Duplex', (30, 110), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0))

cv2.putText(img, 'Simplex', (200, 110), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 250))

cv2.putText(img, 'Complex Small', (30, 180), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,(0, 0, 0))
cv2.putText(img, 'Complex', (30, 220), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))
cv2.putText(img, 'Triplex', (30, 260), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 0))

cv2.putText(img, 'Complex', (200, 260), cv2.FONT_HERSHEY_TRIPLEX, 2, (0, 0, 255))

cv2.putText(img, 'Script Simplex', (30, 330), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0, 0, 0))
cv2.putText(img, 'Script Complex', (30, 370), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (0, 0, 0))

cv2.putText(img, 'Plain Italic', (30, 430), cv2.FONT_HERSHEY_PLAIN | cv2.FONT_ITALIC, 1, (0, 0, 0))
cv2.putText(img, 'Plain Italic', (30, 470), cv2.FONT_HERSHEY_COMPLEX_SMALL | cv2.FONT_ITALIC, 1, (0, 0, 0))

cv2.imshow('img', img)

cv2.waitKey()
cv2.destroyAllWindows()