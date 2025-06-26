import numpy as np

v = np.random.rand(10) * 15 #shape = (10,)

v_col = v[:,None] #shape = (10,1)

print(v_col)

M = np.random.rand(10,3)

print(M)


M = M+v_col

print(M)