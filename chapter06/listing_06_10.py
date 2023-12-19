import numpy as np


def add_matrices_limits(A, B, C, lp, up, lr, ur):
    for i in range(lp, up + 1):
        for k in range(lr, ur + 1):
            C[i, k] = A[i, k] + B[i, k]


def matrix_mult_limits(A, B, C, lp, up, lq, uq, lr, ur):
    mp = (lp + up) // 2
    mq = (lq + uq) // 2
    mr = (lr + ur) // 2

    if lp == up and lq == uq and lr == ur:
        C[mp, mr] = A[mp, mq] * B[mq, mr]
    elif lp <= up and lq <= uq and lr <= ur:

        M1 = np.zeros((A.shape[0], B.shape[1]))
        M2 = np.zeros((A.shape[0], B.shape[1]))

        matrix_mult_limits(A, B, M1, lp, mp, lq, mq, lr, mr)
        matrix_mult_limits(A, B, M2, lp, mp, mq + 1, uq, lr, mr)
        add_matrices_limits(M1, M2, C, lp, mp, lr, mr)

        matrix_mult_limits(A, B, M1, lp, mp, lq, mq, mr + 1, ur)
        matrix_mult_limits(
            A, B, M2, lp, mp, mq + 1, uq, mr + 1, ur)
        add_matrices_limits(M1, M2, C, lp, mp, mr + 1, ur)

        matrix_mult_limits(A, B, M1, mp + 1, up, lq, mq, lr, mr)
        matrix_mult_limits(
            A, B, M2, mp + 1, up, mq + 1, uq, lr, mr)
        add_matrices_limits(M1, M2, C, mp + 1, up, lr, mr)

        matrix_mult_limits(
            A, B, M1, mp + 1, up, lq, mq, mr + 1, ur)
        matrix_mult_limits(
            A, B, M2, mp + 1, up, mq + 1, uq, mr + 1, ur)
        add_matrices_limits(M1, M2, C, mp + 1, up, mr + 1, ur)


def matrix_mult_limits_wrapper(A, B):
    C = np.zeros((A.shape[0], B.shape[1]))
    matrix_mult_limits(A, B, C,
                       0, A.shape[0] - 1, 0, A.shape[1] - 1, 0, B.shape[1] - 1)
    return C


A = np.matrix([[2, 3, 1, -3], [4, -2, 1, 2]])
B = np.matrix([[2, 3, 1], [4, -1, -5], [0, -6, 3], [1, -1, 1]])
print(matrix_mult_limits_wrapper(A, B))


# Test
print()

A = np.matrix([[2]])
B = np.matrix([[-2]])
print(matrix_mult_limits_wrapper(A, B))
print()

A = np.matrix([[2]])
B = np.matrix([[-2, 4, 5]])
print(matrix_mult_limits_wrapper(A, B))
print()

A = np.matrix([[2, 4, 5]])
B = np.matrix([[-2], [4], [5]])
print(matrix_mult_limits_wrapper(A, B))
print()

A = np.matrix([[2, 3, 1, -3]])
B = np.matrix([[2, 3, 1], [4, -1, -5], [0, -6, 3], [1, -1, 1]])
print(matrix_mult_limits_wrapper(A, B))
print()

A = np.matrix([[2], [3], [1], [-3]])
B = np.matrix([[2]])
print(matrix_mult_limits_wrapper(A, B))
print()

A = np.matrix([[2], [3], [1], [-3]])
B = np.matrix([[2, 3, 1]])
print(matrix_mult_limits_wrapper(A, B))
print()

A = np.matrix([[2, 3, 1, -3], [4, -2, 1, 2]])
B = np.matrix([[2], [4], [0], [1]])
print(matrix_mult_limits_wrapper(A, B))
