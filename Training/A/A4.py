import numpy as np

M = np.random.rand(6,6)

sliced = M[3,2:4] #slice [ncol-1,start-1:end]

print(sliced)
print(M)