__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

import math
import numpy as np
import matplotlib.pyplot as plt


def koch_curva(p, q, n):
    if n == 0:     # The base case is just a line segment
        plt.plot([p[0, 0], q[0, 0]], [p[1, 0], q[1, 0]], 'k-')
    else:

        v = q - p
        koch_curva(p, p + v / 3, n - 1)

        R_60 = np.matrix([[math.cos(math.pi / 3),
                           -math.sin(math.pi / 3)],
                          [math.sin(math.pi / 3),
                           math.cos(math.pi / 3)]])

        x = p + v / 3 + R_60 * v / 3
        koch_curva(p + v / 3, x, n - 1)

        koch_curva(x, p + 2 * v / 3, n - 1)

        koch_curva(p + 2 * v / 3, q, n - 1)


def koch_copo_de_nieve(n):
    p = np.array([[0], [0]])
    q = np.array([[1], [0]])
    r = np.array([[0.5], [math.sqrt(3) / 2]])
    koch_curva(p, r, n)
    koch_curva(r, q, n)
    koch_curva(q, p, n)


fig = plt.figure()
fig.patch.set_facecolor('white')
koch_copo_de_nieve(3)
plt.axis('equal')
plt.axis('off')
plt.show()
