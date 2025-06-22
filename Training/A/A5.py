# programmer windows 11
import numpy as np

M = np.random.rand(50,)*5

def vec_mean(vec): #words
    total = 0
    for x in vec:
        total += x
    return total/len(vec)

mask = M > M.mean() # vecteur true/false, true en i si M[i] > M.mean()
print(M.mean())
print(M[mask])
print(M[~mask])