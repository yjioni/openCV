import cv2
from tkinter import *
from tkinter import filedialog

root = Tk()

img_file = filedialog.askopenfilename(
                            title='Choose an image',
                            initialdir='C:/Users/',
                            filetypes=(('jpg files', '*.jpg'),
                                       ('all files', '*.*'))
                            )

img = cv2.imread(img_file)
title = 'Image'
x, y = 100, 100

while True:
    cv2.imshow(title, img)
    cv2.moveWindow(title, x, y)
    key = cv2.waitKey(0) & 0xFF
    print(key, chr(key))
    if key == ord('h'):
        x -= 10
    # 아래로 1
    elif key == ord('j'):
        y += 10
    elif key == ord('k'):
        x += 10
    # 위로 1
    elif key == ord('u'):
        y -=10
    
    elif key == ord('q') or key == 27:
        break
        cv2.destroyAllWindows()
    cv2.moveWindow(title, x, y)


