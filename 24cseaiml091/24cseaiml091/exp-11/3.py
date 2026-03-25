import numpy as np
ones_a=np.ones((2,3))
zeros_a =np.zeros((2,2))
empty_a=np.empty((2,3))
print("ones:\n",ones_a)
print("zeros:\n",zeros_a)
arr=np.arr([1,2,3],[4,5,6])
reshaped = arr.reshape(3,2)
print("reshaped array:\n",reshaped)