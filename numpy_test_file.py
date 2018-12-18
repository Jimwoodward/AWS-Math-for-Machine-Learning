import numpy as np

# this defines a row vector
v = [1, 2, 3]

# this defines a 3x3 matrix
A = [[1, 2, 3], [-1, 0, 1], [1, 1, 1]]

# print the row vector v
print(v, "\n")

# print the matrix A
print(A, "\n")

v_vec = np.array(v)
A_matr = np.matrix(A)

print(v_vec, "\n")
print(A_matr, "\n")
