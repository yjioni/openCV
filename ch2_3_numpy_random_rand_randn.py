import numpy as np

a = np.arange(0, 5+1, step=1, dtype=np.float16)
print(a)
print(a.dtype)
print(a.shape)

b = np.arange(5.0)
print(b)
print(b.dtype)
print(b.shape)

c = np.arange(3, 8+1, 2)
print(c)
print(c.dtype)
print(c.shape)

print(np.random.rand())
print(np.random.randn())

d = np.random.rand(2, 3)
print(d)
print(d.dtype)
print(d.shape)

e = np.random.randn(2, 3)
print(e)
print(e.dtype)
print(e.shape)