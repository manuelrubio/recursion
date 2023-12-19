import numpy as np
import matplotlib.pyplot as plt


def koch_curve(p, q, n):
    if n == 0:   # The base case is just a line segment
        plt.plot([p[0, 0], q[0, 0]], [p[1, 0], q[1, 0]], 'k-')
    else:
        v = q - p
        koch_curve(p, p + v / 3, n - 1)
        R_90 = np.matrix([[0, -1], [1, 0]])
        x = p + v / 3 + R_90 * v / 3
        koch_curve(p + v / 3, x, n - 1)
        y = x + v / 3
        koch_curve(x, y, n - 1)
        koch_curve(y, p + 2 * v / 3, n - 1)
        koch_curve(p + 2 * v / 3, q, n - 1)


def koch_square(n):
    p = np.array([[0], [0]])
    q = np.array([[1], [0]])
    r = np.array([[1], [1]])
    s = np.array([[0], [1]])

    koch_curve(p, q, n)
    koch_curve(q, r, n)
    koch_curve(r, s, n)
    koch_curve(s, p, n)


fig = plt.figure()
fig.patch.set_facecolor('white')
koch_square(4)
plt.axis('equal')
plt.axis('off')
plt.show()
