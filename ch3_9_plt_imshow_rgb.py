import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('./img/girl.jpg')
plt.imshow(img[:, :, ::-1])
plt.xticks([])
plt.yticks([])
plt.show()
