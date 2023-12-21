__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def existe_camino_cienaga(A, r):
    if r < 0 or r >= A.shape[0] or A[r, 0] == 'W':
        return False
    elif A.shape[1] == 1:
        return True
    else:
        return (existe_camino_cienaga(A[:, 1:], r - 1)
                or existe_camino_cienaga(A[:, 1:], r)
                or existe_camino_cienaga(A[:, 1:], r + 1))


# Test
import numpy as np

A = np.matrix([['W', 'W', 'W', 'W', '', '', ''],
               ['', '', 'W', '', 'W', '', 'W'],
               ['W', 'W', '', '', 'W', 'W', ''],
               ['', 'W', 'W', 'W', 'W', '', 'W'],
               ['W', '', '', '', 'W', 'W', 'W']])
print(existe_camino_cienaga(A, 0))
print(existe_camino_cienaga(A, 1))
print(existe_camino_cienaga(A, 2))
print(existe_camino_cienaga(A, 3))
print(existe_camino_cienaga(A, 4))
print()

A = np.matrix([['', '', '', '', '', '', '']])
print(existe_camino_cienaga(A, 0))
print(existe_camino_cienaga(A, 1))
print()

A = np.matrix([['W', 'W', 'W', 'W', '', '', ''],
               ['', '', '', '', 'W', 'W', 'W']])
print(existe_camino_cienaga(A, 0))
print(existe_camino_cienaga(A, 1))
print()

A = np.matrix([['W', 'W', 'W', 'W', '', '', 'W'],
               ['', '', 'W', '', 'W', '', 'W'],
               ['W', 'W', '', '', 'W', 'W', ''],
               ['', '', 'W', '', '', '', 'W']])
print(existe_camino_cienaga(A, 0))
print(existe_camino_cienaga(A, 1))
print(existe_camino_cienaga(A, 2))
print(existe_camino_cienaga(A, 3))
print()

A = np.matrix([['W', 'W', 'W', 'W', '', '', ''],
               ['', '', 'W', '', 'W', '', 'W'],
               ['W', 'W', '', '', 'W', 'W', ''],
               ['', '', 'W', 'W', 'W', 'W', ''],
               ['W', 'W', '', '', '', '', 'W']])
print(existe_camino_cienaga(A, 0))
print(existe_camino_cienaga(A, 1))
print(existe_camino_cienaga(A, 2))
print(existe_camino_cienaga(A, 3))
print(existe_camino_cienaga(A, 4))
print()
