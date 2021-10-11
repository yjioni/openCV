import numpy as np
import cv2

img = np.zeros((120, 120), dtype=np.uint8)
img[25:35, :] = 45
img[45:55, :] = 30
img[:, 25:35] = 30
img[:, 45:55] = 45
img[90:120, 90:120] = 90
img[60:90, 60:90] = 120

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()