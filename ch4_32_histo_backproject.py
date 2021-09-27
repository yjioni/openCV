import cv2
import numpy as np
import matplotlib.pyplot as plt

from tkinter import *
from tkinter import filedialog

root = Tk()
root.filename = filedialog.askopenfilename(title='select an image',
                                    initialdir='C:/Users/',
                                    filetypes=(('jpg files', '*.jpg'),
                                               ('all files', '*.*'))
                                            )

img = cv2.imread(root.filename)
win_name = 'back_project'

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

draw = img.copy()

def masking(bp, win_name):
    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    cv2.filter2D(bp, -1, disc, bp)
    _, mask = cv2.threshold(bp, 1, 255, cv2.THRESH_BINARY)
    result = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow(win_name, result)

def backProject_manual(hist_roi):
    hist_img = cv2.calcHist([hsv_img], [0, 1], None, [180, 256], [0,180,0,256])
    hist_rate = hist_roi/(hist_img+1)

    h, s, v = cv2.split(hsv_img)
    bp = hist_rate[h.ravel(), s.ravel()]
    bp = np.minimum(bp, 1)
    bp = bp.reshape(hsv_img.shape[:2])
    cv2.normalize(bp, bp, 0, 255, cv2.NORM_MINMAX)
    bp = bp.astype(np.uint8)
    masking(bp, 'result_manual')

def backProject_cv(hist_roi):
# cv2.calcBackProject([img], channel, 역투영에 사용할 히스토그램, 각 픽셀 값 범위, 배율 계수)
    bp = cv2.calcBackProject([hsv_img], [0,1], hist_roi, [0,180,0,256], 1)
    masking(bp, 'result_cv')

# 마우스로 사각형 영역 설정해서 좌표 얻음
# ROI = Region of Interest
(x, y, w, h) = cv2.selectROI(windowName=win_name, img=img, showCrosshair=False, fromCenter=False)

if w > 0 and h > 0:
    roi = draw[y:y+h, x:x+w]
    # 이미지 위에 사각형 그리기
    cv2.rectangle(draw, (x,y), (x+w, y+h), (0,0,256), 2)
    
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    hist_roi = cv2.calcHist([hsv_roi], [0,1], None, [180,256], [0,180,0,256])
    backProject_manual(hist_roi)
#     backProject_cv(hist_roi)

# cv2.imshow(win_name, draw)
# cv2.waitKey()
# cv2.destroyAllWindows()
