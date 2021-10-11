import numpy as np

a = np.array([1, 2, 3, 4])
print(a)
print(a.dtype)
print(a.shape)

b = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(b)
print(b.dtype)
print(b.shape)

c = np.array([1, 2, 3.14, 4])
print(c)
print(c.dtype)
print(c.shape)

d = np.array([1, 2, 3, 4], dtype=np.float32)
print(d)
print(d.dtype)
print(d.shape)

e = np.array([1, 2, 3, 4], dtype=np.uint8)
print(e)
print(e.dtype)
print(e.shape)

f = np.uint8([1, 2, 3, 4])
print(f)
print(f.dtype)
print(f.shape)