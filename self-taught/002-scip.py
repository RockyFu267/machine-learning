import numpy as np
from scipy import sparse

matrix01 = np.eye(6)
sparse_matrix = sparse.csr_matrix(matrix01)
print("对角矩阵： \n{}".format(matrix01))
print("\nsparse存储的矩阵： \n{}".format(sparse_matrix))
