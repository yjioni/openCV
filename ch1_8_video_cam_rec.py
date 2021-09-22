import cv2
from tkinter import *
from tkinter import filedialog

root = Tk()
root.savename = filedialog.asksaveasfilename(
    initialdir='C:/',
    title='save name as',
    filetypes=(('avi files', '*.avi'), ('all files', '*.*'))
    )
save_file = f'{root.savename}.avi'

cap = cv2.VideoCapture(0)

if cap.isOpened:
    file_path = save_file
    fps = 25.40 # frame per seconds
    fourcc = cv2.VideoWriter_fourcc(*'DIVX') # incoding format char
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    size = (int(width), int(height))
    print('origin szie:', size)
    out = cv2.VideoWriter(file_path, fourcc, fps, size)

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('camera-recording', frame)
            out.write(frame)
            if cv2.waitKey(int(1000/fps)) != -1:
                break
        else:
            print('no frame')
            break
else:
    print('cannot open camera')
cap.release()
cv2.destroyAllWindows()