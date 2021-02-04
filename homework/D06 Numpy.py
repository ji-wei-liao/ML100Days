import numpy as np

array1 = np.array(range(30))
array2 = np.array([2,3,5])

with open('array.npz','wb') as f:
    np.savez(f,array1,array2)
    
load_array=np.load('array.npz')
array3=np.array([[4,5,6],[1,2,3]])
np.savez('new_array.npz',load_array,array3)