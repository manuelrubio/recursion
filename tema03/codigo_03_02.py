__copyright__ = "Copyright (C) 2023 Manuel Rubio S�nchez"
__license__ = "MIT License"

import numpy as np

A = np.array([[1, 0, 0, 1], [1, 1, 1, 2],
              [1, 2, 4, 4], [1, 3, 9, 8]])
b = np.array([0, 2, 11, 28])
x = np.linalg.solve(A, b)


# Prueba
print(x)
