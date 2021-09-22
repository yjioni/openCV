import cv2
from tkinter import *
from tkinter import filedialog

root = Tk()
root.avi_file = filedialog.askopenfilename(
    initialdir='C:/Users/',
    title='Select an avi file',
    filetypes=(('avi files', '*.avi'), ('all files', '*.*'))
    )

video_file = root.avi_file

cap = cv2.VideoCapture(video_file)

if cap.isOpened():
    while True:
        ret, img = cap.read()
        print(cap.read())
        if ret:
            cv2.imshow(video_file, img)
            cv2.waitKey(25)
        else:
            break
else:
    print('can\'t open video.')

cap.release()
cv2.destroyAllWindows()
