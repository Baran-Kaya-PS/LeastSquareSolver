import numpy as np

x = [v for v in range(0,120)]

x = np.array(x)

print(f"x at first = {x}\n")

print(f"Shape = {x.shape}\n")

print(f"dtype = {x.dtype}\n")

x = x.reshape(12,10)

print(f"x after reshape : \n{x}\n")

print(f"Shape of x after reshape : {x.shape}\n")

print(f"his type {x.dtype}\n")