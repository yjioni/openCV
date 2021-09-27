import cv2
import numpy as np

from tkinter import *
from tkinter import filedialog

# alpha blending rate : 20%
alpha_width_rate = 20

img_face = cv2.imread(filedialog.askopenfilename())
img_skull = cv2.imread(filedialog.askopenfilename())

img_comp = np.zeros_like(img_face)

height, width = img_face.shape[:2]
middle = width // 2
alpha_width = width * alpha_width_rate // 100
start = middle - alpha_width // 2
step = 100/alpha_width

img_comp[:, middle:, :] = img_face[:, middle:, :].copy()
img_comp[:, :middle, :] = img_skull[:, :middle, :].copy()

cv2.imshow('half_only', img_comp)

for i in range(alpha_width+1):
    alpha = (100-step*i)/100
    beta = 1-alpha
    
    img_comp[:, start+i] = img_skull[:, start+i]*alpha+img_face[:, start+i]*beta

    print(i, alpha, beta)

cv2.imshow('half_blending', img_comp)
cv2.waitKey()
cv2.destroyAllWindows()