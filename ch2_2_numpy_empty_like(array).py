import numpy as np
import cv2

a = np.empty((2, 3))
print(a)
print(a.dtype)
print(a.shape)

b = np.zeros((2, 3), dtype=np.uint8)
print(b)
print(b.dtype)
print(b.shape)

c = np.ones((2, 3), dtype=np.uint8)
print(c)
print(c.dtype)
print(c.shape)

d = np.full((2, 3), 3, dtype=np.float16)
print(d)
print(d.dtype)
print(d.shape)

d.fill(2)
print(d)
print(d.dtype)
print(d.shape)

img = cv2.imread('C:/Users/oing9/Documents/Crawling/img/girl.jpg')
print(img)
print(img.dtype)
print(img.shape)

A = np.empty_like(img)
B = np.zeros_like(img)
C = np.ones_like(img)
D = np.full_like(img, 255)

print(A)
print(A.dtype)
print(A.shape)
print(B)
print(B.dtype)
print(B.shape)
print(C)
print(C.dtype)
print(C.shape)
print(D)
print(D.dtype)
print(D.shape)
