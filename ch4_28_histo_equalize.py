import cv2
import numpy as np
import matplotlib.pylab as plt

from tkinter import *
from tkinter import filedialog

root = Tk()
root.filename = filedialog.askopenfilename(title='select an image',
                                    initialdir='C:/Users/',
                                    filetypes=(('jpg files', '*.jpg'),
                                               ('all files', '*.*'))
                                            )

img = cv2.imread(root.filename, cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape[:2]
hist = cv2.calcHist([img], [0], None, [256], [0, 256])


# 누적 히스토그램
cdf = hist.cumsum() 
# 0인 값을 NaN으로 설정 ... 연산을 줄이기 위함(속도개선)
cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min())/(rows*cols)*255
# NaN을 0으로 다시 설정
cdf = np.ma.filled(cdf_m,0).astype('uint8')
# 히스토그램을 픽셀로 매칭
img2 = cdf[img]
hist2 = cv2.calcHist([img2], [0], None, [256], [0, 256])


## 이퀄라이즈 함수
img3 = cv2.equalizeHist(img)
hist3 = cv2.calcHist([img3], [0], None, [256], [0, 256])


cv2.imshow('before', img)
cv2.imshow('manual', img2)
cv2.imshow('equalizeHist', img3)

hists = {'before':hist, 'manual':hist2, 'equalizeHist':hist3}
for i, (k, v) in enumerate(hists.items()):
    plt.subplot(1, 3, i+1)
    plt.title(k)
    plt.plot(v)

plt.show()

cv2.waitKey()
cv2.destroyAllWindows()
