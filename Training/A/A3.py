import numpy as np
import random

M = np.zeros((5,5))

for x in range(len(M)):
    for y in range(len(M[0])):
        if x == y:
            M[x,y] = 1
        elif x < y:
            M[x,y] = random.randint(1, 10)
print(M)