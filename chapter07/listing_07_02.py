def exists_path_swamp_alt(A, r):
    if A.shape[1] == 1:
        return A[r, 0] != 'W'
    else:
        if r == 0 or A[r - 1, 1] == 'W':
            diag_up = False
        else:
            diag_up = exists_path_swamp_alt(A[:, 1:], r - 1)

        if not diag_up:
            if r == A.shape[0] - 1 or A[r + 1, 1] == 'W':
                diag_down = False
            else:
                diag_down = exists_path_swamp_alt(
                    A[:, 1:], r + 1)

            if not diag_down:
                if A[r, 1] == 'W':
                    horizontal = False
                else:
                    horizontal = exists_path_swamp_alt(
                        A[:, 1:], r)

        return diag_up or diag_down or horizontal


# Test
import numpy as np

A = np.matrix([['W', 'W', 'W', 'W', '·', '·', '·'],
               ['·', '·', 'W', '·', 'W', '·', 'W'],
               ['W', 'W', '·', '·', 'W', 'W', '·'],
               ['·', 'W', 'W', 'W', 'W', '·', 'W'],
               ['W', '·', '·', '·', 'W', 'W', 'W']])
print(exists_path_swamp_alt(A, 1))
print(exists_path_swamp_alt(A, 3))
print()

A = np.matrix([['·', '·', '·', '·', '·', '·', '·']])
print(exists_path_swamp_alt(A, 0))
print()

A = np.matrix([['W', 'W', 'W', 'W', '·', '·', '·'],
               ['·', '·', '·', '·', 'W', 'W', 'W']])
print(exists_path_swamp_alt(A, 1))
print()

A = np.matrix([['W', 'W', 'W', 'W', '·', '·', 'W'],
               ['·', '·', 'W', '·', 'W', '·', 'W'],
               ['W', 'W', '·', '·', 'W', 'W', '·'],
               ['·', '·', 'W', '·', '·', '·', 'W']])
print(exists_path_swamp_alt(A, 1))
print(exists_path_swamp_alt(A, 3))
print()

A = np.matrix([['W', 'W', 'W', 'W', '·', '·', '·'],
               ['·', '·', 'W', '·', 'W', '·', 'W'],
               ['W', 'W', '·', '·', 'W', 'W', '·'],
               ['·', '·', 'W', 'W', 'W', 'W', '·'],
               ['W', 'W', '·', '·', '·', '·', 'W']])
print(exists_path_swamp_alt(A, 1))
print(exists_path_swamp_alt(A, 3))
print()
