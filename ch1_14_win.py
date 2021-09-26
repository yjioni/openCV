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
img_gray = cv2.imread(root.filename, cv2.IMREAD_GRAYSCALE)

# WINDOW_AUTOSIZE == jpg 파일 사이즈로 윈도우창 설정
cv2.namedWindow('origin', cv2.WINDOW_AUTOSIZE)
# WINDOW_NORMAL == 윈도우창 크기 변경 가능
cv2.namedWindow('gray_ver', cv2.WINDOW_NORMAL)

cv2.imshow('origin', img)
cv2.imshow('gray_ver', img_gray)

# 윈도우 창 위치
cv2.moveWindow('origin', 0, 0)
cv2.moveWindow('gray_ver', 100, 100)

# 버튼을 누르면
cv2.waitKey()
# 윈도우 창 사이즈 변경
# AUTOSIZE로 열었던 것은 윈도우 창 사이즈만 변경 
# NORMAL로 열었던 것은 윈도우 창 사이즈에 맞춰 그림 사이즈 변경

cv2.resizeWindow('origin', 200, 100)
cv2.resizeWindow('gray_ver', 200, 200)

cv2.waitKey()
cv2.destroyWindow('gray_ver')

cv2.waitKey()
cv2.destroyAllWindows()