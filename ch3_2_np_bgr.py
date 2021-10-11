import numpy as np
import cv2

img = np.zeros((120, 120, 3), dtype=np.uint8)

img[25:35, :] = [255,0,0]
img[45:55, :] = [255,255,0]
img[:, 25:35] = [0,0,255]
img[:, 45:55] = [0,255,255]
img[65:75, 65:75] = [0,255,0]
img[75:85, 75:85] = [100,100,100]
img[85:95, 85:95] = [120,255,120]
# print(img.shape)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()