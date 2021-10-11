import cv2
import numpy as np

def nprint(arr):
    # array type출력 보통 <class 'numpy.ndarray'>
    print('type: {}'.format(type(arr)))  
    # shape: 행렬 모양, dimension: 차원, dtype: 원소 type
    print('shape: {}, dimension: {}, dtype: {}'.format(arr.shape, arr.ndim, arr.dtype))
    # array 출력
    print("array:\n", arr)

img = cv2.imread('C:/Users/oing9/Documents/Crawling/img/4star.jpg')
nprint(img)


a = np.array([[[1, 2], [3, 4], [5, 6]],
     [[7, 8], [9, 0], [-1, -2]],
     [[1, 2], [3, 4], [5, 6]],
     [[1, 2], [3, 4], [5, 6]]
     ])
nprint(a)

print(a[1,1,1])