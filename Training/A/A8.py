import time
import numpy as np

M1 = np.random.rand(500,500)

M2 = np.random.rand(500,500)

start = time.time()
M3 = M1 + M2
end = time.time()

print(f"Elapsed : {end - start} seconds")
def matadd_(A,B):
    if np.shape(A) == np.shape(B):
        m,n = A.shape
        M3 = np.zeros_like(A)
        for i in range(m):
            for j in range(n):
                M3[i,j] = A[i,j] + B[i,j]
        return M3
    return None

start = time.time()
M3 = matadd_(M1,M2)
end = time.time()
print(f"Elapsed : {end - start} seconds")