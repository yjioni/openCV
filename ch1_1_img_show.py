import cv2
from tkinter import *
from tkinter import filedialog

root = Tk()
root.filename = filedialog.askopenfilename(
    initialdir = 'C:',
    title = 'img file',
    filetypes = (('jpg files', '*.jpg'), ('all files', '*.*'))
    )

print(root.filename)

img = cv2.imread(root.filename, cv2.IMREAD_GRAYSCALE)

if img is not None:
    cv2.imshow(root.filename, img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print('이미지 파일 확인 요망')
    