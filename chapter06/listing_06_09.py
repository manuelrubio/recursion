import numpy as np


def matrix_mult(A, B):
    p = A.shape[0]
    q = A.shape[1]
    r = B.shape[1]

    if p == 0 or q == 0 or r == 0:
        return np.zeros((p, r))
    elif p == 1 and q == 1 and r == 1:
        return np.matrix([[A[0, 0] * B[0, 0]]])
    else:
        A11 = A[0:p // 2, 0:q // 2]
        A21 = A[p // 2:p, 0:q // 2]
        A12 = A[0:p // 2, q // 2:q]
        A22 = A[p // 2:p, q // 2:q]

        B11 = B[0:q // 2, 0:r // 2]
        B21 = B[q // 2:q, 0:r // 2]
        B12 = B[0:q // 2, r // 2:r]
        B22 = B[q // 2:q, r // 2:r]

        C11 = matrix_mult(A11, B11) + matrix_mult(A12, B21)
        C12 = matrix_mult(A11, B12) + matrix_mult(A12, B22)
        C21 = matrix_mult(A21, B11) + matrix_mult(A22, B21)
        C22 = matrix_mult(A21, B12) + matrix_mult(A22, B22)

        return np.vstack([np.hstack([C11, C12]),
                          np.hstack([C21, C22])])


A = np.matrix([[2, 3, 1, -3], [4, -2, 1, 2]])
B = np.matrix([[2, 3, 1], [4, -1, -5], [0, -6, 3], [1, -1, 1]])
print(matrix_mult(A, B))


# Test
print()

A = np.matrix([[2]])
B = np.matrix([[-2]])
print(matrix_mult(A, B))
print()

A = np.matrix([[2]])
B = np.matrix([[-2, 4, 5]])
print(matrix_mult(A, B))
print()

A = np.matrix([[2, 4, 5]])
B = np.matrix([[-2], [4], [5]])
print(matrix_mult(A, B))
print()

A = np.matrix([[2, 3, 1, -3]])
B = np.matrix([[2, 3, 1], [4, -1, -5], [0, -6, 3], [1, -1, 1]])
print(matrix_mult(A, B))
print()

A = np.matrix([[2], [3], [1], [-3]])
B = np.matrix([[2]])
print(matrix_mult(A, B))
print()

A = np.matrix([[2], [3], [1], [-3]])
B = np.matrix([[2, 3, 1]])
print(matrix_mult(A, B))
print()

A = np.matrix([[2, 3, 1, -3], [4, -2, 1, 2]])
B = np.matrix([[2], [4], [0], [1]])
print(matrix_mult(A, B))
