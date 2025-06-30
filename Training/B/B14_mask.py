import numpy as np

x = np.random.rand(10)
mask = ((x > 0.2) & (x < 0.8)) | (x < 0)

print(x)
print(x[mask])