import numpy as np

array1 = np.array(range(30))
array2 = np.array([2,3,5])

with open('multi_array.npz','wb') as f:
    np.savez(f,array1,array2)