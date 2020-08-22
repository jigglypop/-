import numpy as np


arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr = np.rot90(arr)
print(arr)
arr = np.rot90(arr)
print(arr)
arr = np.rot90(arr)
print(arr)
arr = np.rot90(arr)
print(arr)
pad = ((2, 2), (2, 2))
arr_pad = np.pad(arr, pad, 'constant', constant_values=(0))
print(arr_pad)
