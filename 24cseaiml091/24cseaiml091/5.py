import numpy as np
a= np.array([1,2,3,4]) 
np.save("my_array",a)
load_array=np.load("my_array".npy)
print("loaded array:",load_array)
