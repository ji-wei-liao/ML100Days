import numpy as np
array1=np.array(range(30))
array1=array1.reshape((5,6),order ="F")

np.where(array1 % 6 ==1)

