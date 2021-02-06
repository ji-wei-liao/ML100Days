import numpy as np
array1=np.array([10,8],[3,5])
array1_inv=np.linalg.inv(array1)
np.dot(array1_inv,array1)

w,v=np.linalg.eig(array1)
print(w)
print(v)

np.linalg.svd(array1)