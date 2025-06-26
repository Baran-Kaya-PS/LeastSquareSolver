import numpy as np

v = np.random.rand(3)*15
M = np.random.rand(7,3)
print("before")
print(M)
M = M+v
print("after")
print(M)