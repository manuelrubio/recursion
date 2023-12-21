__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

import numpy as np
import matplotlib.pyplot as plt


def koch_curva(p, q, n):
    if n == 0:   # El caso base es solo un segmento
        plt.plot([p[0, 0], q[0, 0]], [p[1, 0], q[1, 0]], 'k-')
    else:
        v = q - p
        koch_curva(p, p + v / 3, n - 1)
        R_90 = np.matrix([[0, -1], [1, 0]])
        x = p + v / 3 + R_90 * v / 3
        koch_curva(p + v / 3, x, n - 1)
        y = x + v / 3
        koch_curva(x, y, n - 1)
        koch_curva(y, p + 2 * v / 3, n - 1)
        koch_curva(p + 2 * v / 3, q, n - 1)


def koch_cuadrado(n):
    p = np.array([[0], [0]])
    q = np.array([[1], [0]])
    r = np.array([[1], [1]])
    s = np.array([[0], [1]])

    koch_curva(p, q, n)
    koch_curva(q, r, n)
    koch_curva(r, s, n)
    koch_curva(s, p, n)


fig = plt.figure()
fig.patch.set_facecolor('white')
koch_cuadrado(4)
plt.axis('equal')
plt.axis('off')
plt.show()
