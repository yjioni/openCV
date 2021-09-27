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

img = cv2.imread(root.filename)


img_f = img.astype(np.float32)
img_norm = ((img_f-img_f.min())*(255) / (img_f.max()-img_f.min()))
img_norm = img_norm.astype(np.uint8)

# normalize func
# cv2.normalize(변경전, 변경후, 구간1, 구간2, type_flag)
# *type_flag = NORM_MINMAX(구간), NORM_L1, NORM_L2, NORM_INF

img_norm2 = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)


hist = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_norm = cv2.calcHist([img_norm], [0], None, [256], [0, 256])
hist_norm2 = cv2.calcHist([img_norm2], [0], None, [256], [0, 256])

cv2.imshow('Before', img)
cv2.imshow('manual', img_norm)
cv2.imshow('normalize', img_norm2)


hists = {'before':hist, 'manual':hist_norm, 'normalize':hist_norm2}
for i, (k, v) in enumerate(hists.items()):
    plt.subplot(1, 3, i+1)
    plt.title(k)
    plt.plot(v)


plt.show()
cv2.waitKey()
cv2.destroyAllWindows()


