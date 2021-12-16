import numpy as np

x = np.zeros((5,5),dtype=int)
print(x.shape)
print(x)
print(x.ndim)
x.reshape(1,5*5)
print(x)
print(x.shape)
print(x.ndim)
print("*"*100)
