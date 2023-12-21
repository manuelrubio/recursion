__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

import numpy as np


def suma_matrices_limites(A, B, C, lp, up, lr, ur):
    for i in range(lp, up + 1):
        for k in range(lr, ur + 1):
            C[i, k] = A[i, k] + B[i, k]


def multiplica_matrices_limites(A, B, C, lp, up, lq, uq, lr, ur):
    mp = (lp + up) // 2
    mq = (lq + uq) // 2
    mr = (lr + ur) // 2

    if lp == up and lq == uq and lr == ur:
        C[mp, mr] = A[mp, mq] * B[mq, mr]
    elif lp <= up and lq <= uq and lr <= ur:

        M1 = np.zeros((A.shape[0], B.shape[1]))
        M2 = np.zeros((A.shape[0], B.shape[1]))

        multiplica_matrices_limites(A, B, M1, lp, mp, lq, mq, lr, mr)
        multiplica_matrices_limites(A, B, M2, lp, mp, mq + 1, uq, lr, mr)
        suma_matrices_limites(M1, M2, C, lp, mp, lr, mr)

        multiplica_matrices_limites(A, B, M1, lp, mp, lq, mq, mr + 1, ur)
        multiplica_matrices_limites(
            A, B, M2, lp, mp, mq + 1, uq, mr + 1, ur)
        suma_matrices_limites(M1, M2, C, lp, mp, mr + 1, ur)

        multiplica_matrices_limites(A, B, M1, mp + 1, up, lq, mq, lr, mr)
        multiplica_matrices_limites(
            A, B, M2, mp + 1, up, mq + 1, uq, lr, mr)
        suma_matrices_limites(M1, M2, C, mp + 1, up, lr, mr)

        multiplica_matrices_limites(
            A, B, M1, mp + 1, up, lq, mq, mr + 1, ur)
        multiplica_matrices_limites(
            A, B, M2, mp + 1, up, mq + 1, uq, mr + 1, ur)
        suma_matrices_limites(M1, M2, C, mp + 1, up, mr + 1, ur)


def multiplica_matrices_limites_wrapper(A, B):
    C = np.zeros((A.shape[0], B.shape[1]))
    multiplica_matrices_limites(A, B, C,
                       0, A.shape[0] - 1, 0, A.shape[1] - 1, 0, B.shape[1] - 1)
    return C


A = np.matrix([[2, 3, 1, -3], [4, -2, 1, 2]])
B = np.matrix([[2, 3, 1], [4, -1, -5], [0, -6, 3], [1, -1, 1]])
print(multiplica_matrices_limites_wrapper(A, B))


# Test
print()

A = np.matrix([[2]])
B = np.matrix([[-2]])
print(multiplica_matrices_limites_wrapper(A, B))
print()

A = np.matrix([[2]])
B = np.matrix([[-2, 4, 5]])
print(multiplica_matrices_limites_wrapper(A, B))
print()

A = np.matrix([[2, 4, 5]])
B = np.matrix([[-2], [4], [5]])
print(multiplica_matrices_limites_wrapper(A, B))
print()

A = np.matrix([[2, 3, 1, -3]])
B = np.matrix([[2, 3, 1], [4, -1, -5], [0, -6, 3], [1, -1, 1]])
print(multiplica_matrices_limites_wrapper(A, B))
print()

A = np.matrix([[2], [3], [1], [-3]])
B = np.matrix([[2]])
print(multiplica_matrices_limites_wrapper(A, B))
print()

A = np.matrix([[2], [3], [1], [-3]])
B = np.matrix([[2, 3, 1]])
print(multiplica_matrices_limites_wrapper(A, B))
print()

A = np.matrix([[2, 3, 1, -3], [4, -2, 1, 2]])
B = np.matrix([[2], [4], [0], [1]])
print(multiplica_matrices_limites_wrapper(A, B))
