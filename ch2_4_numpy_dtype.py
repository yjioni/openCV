import numpy as np

a = np.arange(5)
print(a)
print(a.dtype)
print(a.shape)

b = a.astype('float32')
print(b)
print(b.dtype)
print(b.shape)

c = a.astype(np.float32)
print(c)
print(c.dtype)
print(c.shape)

d = np.uint8(a)
print(d)
print(d.dtype)
print(d.shape)

print(d.size)
print(d.itemsize)

print(np.arange(100).reshape(2, -1))
A = np.random.rand(2, 3)
print(A)
B = A.reshape(6, -1)
print(B)

print('np.ravel(A):', np.ravel(A))
print('reshape(-1):', A.reshape(-1))
print('reshape(1, -1):', A.reshape(1, -1))
print(np.ravel(A).shape)
print(np.reshape(A, -1).shape)
print(A.reshape(1, -1).shape)

g = np.arange(10).reshape(2, -1)
print('g:', g)
print('g.shape:', g.shape)
print('g.size:', g.size)
print('g.itemsize:', g.itemsize)