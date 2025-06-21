import numpy as np

def load_csv(path):
    data = np.loadtxt(path,delimiter=',',skiprows=1)
    A = data[:,:-1]
    b = data[:,-1]
    return A,b