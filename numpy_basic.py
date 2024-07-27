import numpy as np


#Creating an array:
n_array = np.array([1,2,3,4,5,6,7,8,9,10])


#Finding the datatype of the array:
print(n_array.dtype)     #Result = int64


#Finding the shape of the array:
print(n_array.shape)     #Result = (10,)


#Finding the dimension of the array:
print(n_array.ndim)      #Result = 1


#Finding total size of the array:
print(n_array.size)      #Result = 10


#Finding the size in bytes of each element:
print(n_array.itemsize)  #Result = 8