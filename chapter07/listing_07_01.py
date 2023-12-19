def exists_path_swamp(A, r):
    if r < 0 or r >= A.shape[0] or A[r, 0] == 'W':
        return False
    elif A.shape[1] == 1:
        return True
    else:
        return (exists_path_swamp(A[:, 1:], r - 1)
                or exists_path_swamp(A[:, 1:], r)
                or exists_path_swamp(A[:, 1:], r + 1))


# Test
import numpy as np

A = np.matrix([['W', 'W', 'W', 'W', '·', '·', '·'],
               ['·', '·', 'W', '·', 'W', '·', 'W'],
               ['W', 'W', '·', '·', 'W', 'W', '·'],
               ['·', 'W', 'W', 'W', 'W', '·', 'W'],
               ['W', '·', '·', '·', 'W', 'W', 'W']])
print(exists_path_swamp(A, 0))
print(exists_path_swamp(A, 1))
print(exists_path_swamp(A, 2))
print(exists_path_swamp(A, 3))
print(exists_path_swamp(A, 4))
print()

A = np.matrix([['·', '·', '·', '·', '·', '·', '·']])
print(exists_path_swamp(A, 0))
print(exists_path_swamp(A, 1))
print()

A = np.matrix([['W', 'W', 'W', 'W', '·', '·', '·'],
               ['·', '·', '·', '·', 'W', 'W', 'W']])
print(exists_path_swamp(A, 0))
print(exists_path_swamp(A, 1))
print()

A = np.matrix([['W', 'W', 'W', 'W', '·', '·', 'W'],
               ['·', '·', 'W', '·', 'W', '·', 'W'],
               ['W', 'W', '·', '·', 'W', 'W', '·'],
               ['·', '·', 'W', '·', '·', '·', 'W']])
print(exists_path_swamp(A, 0))
print(exists_path_swamp(A, 1))
print(exists_path_swamp(A, 2))
print(exists_path_swamp(A, 3))
print()

A = np.matrix([['W', 'W', 'W', 'W', '·', '·', '·'],
               ['·', '·', 'W', '·', 'W', '·', 'W'],
               ['W', 'W', '·', '·', 'W', 'W', '·'],
               ['·', '·', 'W', 'W', 'W', 'W', '·'],
               ['W', 'W', '·', '·', '·', '·', 'W']])
print(exists_path_swamp(A, 0))
print(exists_path_swamp(A, 1))
print(exists_path_swamp(A, 2))
print(exists_path_swamp(A, 3))
print(exists_path_swamp(A, 4))
print()
