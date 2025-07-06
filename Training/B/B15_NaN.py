import numpy as np
from keras.utils.layer_utils import print_summary


def gen_random_mat(n_rows,n_cols,seed=None) -> np.ndarray:
    if n_cols <= 0 or n_rows <= 0:
        raise ValueError("nrows ou ncols doivent être positifs")
    rng = np.random.default_rng(seed)
    return rng.random((n_rows,n_cols))

def insert_nans(mat,nan_ratio=0.1,seed=None) :#-> np.ndarray:
    if not (0 <= nan_ratio <= 1):
        raise ValueError("nan_ration doit être entre 0 et 1")
    n_rows, n_cols = mat.shape
    rng = np.random.default_rng(seed)
    for i in range(n_rows):
        for j in range(n_cols):
            if rng.random() < nan_ratio:
                mat[i,j] = np.nan
    return mat

def count_nans(mat) -> int:
    pass

def nans_by_cols(mat) -> np.ndarray[int]:
    pass

def col_means(mat) -> np.ndarray[int]:
    pass

def fill_nans_with_col_mean(mat,inplace=False)-> np.ndarray:
    pass

M = gen_random_mat(3,3)

print(M)

print(insert_nans(M))