import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('./img/girl.jpg')

plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(img[:,:,::-1])

plt.show()
