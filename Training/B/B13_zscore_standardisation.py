import numpy as np

A = np.random.rand(5,5)

means = A.mean(axis=0,keepdims=True) #axis => means on cols, keepdims make shape (1,k)
stds = A.std(axis=0,keepdims=True)

Z = ((A-means))/stds # plus rapide que d'extraire chaque col etc...

print(Z)