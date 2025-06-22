import numpy as np

M1 = np.random.rand(3,)
M2 = np.random.rand(3,)
M3 = np.random.rand(3,)

Mvstack = np.vstack((M1,M2,M3))

Mhstack = np.hstack((M1.T,M2.T,M3.T))

print("vecteurs")
print(M1,M2,M3)

print("vstack")
print(Mvstack)

print("hstack")
print(Mhstack)