import numpy as np

arr = np.random.rand(5,5)
print(arr)

with open('test.npy',"wb") as f:
    print("Saving")
    np.save(f,arr)


with open('test.npy','rb') as f:
    print("Loading")
    print(np.load(f))
