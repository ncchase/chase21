import numpy as np

arr = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

arr = np.delete(arr, 1, 0)

print(arr)