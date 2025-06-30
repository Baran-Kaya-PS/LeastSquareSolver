import numpy as np
from keras.utils.layer_utils import print_summary


def gen_random_mat(n_rows,n_cols,low=0.0,high=1,seed=None) -> np.ndarray:
    pass

def insert_nans(mat,nan_ratio=0.1,seed=None) -> np.ndarray:
    pass

def count_nans(mat) -> int:
    pass

def nans_by_cols(mat) -> np.ndarray[int]:
    pass

def col_means(mat) -> np.ndarray[int]:
    pass

def fill_nans_with_col_mean(mat,inplace=False)-> np.ndarray:
    pass

def print_summary(mat):
    pass