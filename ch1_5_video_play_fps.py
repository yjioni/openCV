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
    fps = cap.get(cv2.CAP_PROP_FPS)
    delay = int(1000/fps)
    print('fps: %f, delay: %dms'%(fps, delay))

    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow(video_file, img)
            cv2.waitKey(delay)
        else:
            break
else:
    print('cannot find a video')
cap.release()
cv2.destroyAllWindows()