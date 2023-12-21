__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def existe_camino_cienaga_alt(A, r):
    if A.shape[1] == 1:
        return A[r, 0] != 'W'
    else:
        if r == 0 or A[r - 1, 1] == 'W':
            diag_arriba = False
        else:
            diag_arriba = existe_camino_cienaga_alt(A[:, 1:], r - 1)

        if not diag_arriba:
            if r == A.shape[0] - 1 or A[r + 1, 1] == 'W':
                diag_abajo = False
            else:
                diag_abajo = existe_camino_cienaga_alt(
                    A[:, 1:], r + 1)

            if not diag_abajo:
                if A[r, 1] == 'W':
                    horizontal = False
                else:
                    horizontal = existe_camino_cienaga_alt(
                        A[:, 1:], r)

        return diag_arriba or diag_abajo or horizontal


# Test
import numpy as np

A = np.matrix([['W', 'W', 'W', 'W', '', '', ''],
               ['', '', 'W', '', 'W', '', 'W'],
               ['W', 'W', '', '', 'W', 'W', ''],
               ['', 'W', 'W', 'W', 'W', '', 'W'],
               ['W', '', '', '', 'W', 'W', 'W']])
print(existe_camino_cienaga_alt(A, 1))
print(existe_camino_cienaga_alt(A, 3))
print()

A = np.matrix([['', '', '', '', '', '', '']])
print(existe_camino_cienaga_alt(A, 0))
print()

A = np.matrix([['W', 'W', 'W', 'W', '', '', ''],
               ['', '', '', '', 'W', 'W', 'W']])
print(existe_camino_cienaga_alt(A, 1))
print()

A = np.matrix([['W', 'W', 'W', 'W', '', '', 'W'],
               ['', '', 'W', '', 'W', '', 'W'],
               ['W', 'W', '', '', 'W', 'W', ''],
               ['', '', 'W', '', '', '', 'W']])
print(existe_camino_cienaga_alt(A, 1))
print(existe_camino_cienaga_alt(A, 3))
print()

A = np.matrix([['W', 'W', 'W', 'W', '', '', ''],
               ['', '', 'W', '', 'W', '', 'W'],
               ['W', 'W', '', '', 'W', 'W', ''],
               ['', '', 'W', 'W', 'W', 'W', ''],
               ['W', 'W', '', '', '', '', 'W']])
print(existe_camino_cienaga_alt(A, 1))
print(existe_camino_cienaga_alt(A, 3))
print()
