import cv2
from tkinter import *
from tkinter import filedialog

root = Tk()
root.filename = filedialog.askopenfilename(
    initialdir='C:/',
    title='please select the image what you want to',
    filetypes=(('jpg files', '*.jpg'), ('all files', '*.*'))
    )
print(root.filename)

img_file = cv2.imread(root.filename, cv2.IMREAD_GRAYSCALE)

root.savename = filedialog.asksaveasfilename(
    initialdir='C:/',
    title='save name as',
    filetypes=(('jpg files', '*.jpg'), ('all files', '*.*'))
    )
save_file = f'{root.savename}.jpg'
print(save_file)

if img_file is not None:
    cv2.imshow('img', img_file)
    cv2.imwrite(save_file, img_file)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print('Please check again.')


