import numpy as np

A = np.random.rand(5,5)

def transpose_list(M:np.ndarray):
    M_T = np.zeros_like(M)
    m,n = np.shape(M)
    for i in range(m):
        for j in range(n):
            M_T[i,j] = M[j,i]
    return M_T

print(A.transpose() == transpose_list(A))