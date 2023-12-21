__copyright__ = "Copyright (C) 2023 Manuel Rubio S�nchez"
__license__ = "MIT License"

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def alfombra_sierpinski(ax, p, n, size):
    if n > 0:
        ax.add_patch(Rectangle((p[0, 0] - size / 6,
                                p[1, 0] - size / 6),
                               size / 3, size / 3,
                               facecolor=(0.5, 0.5, 0.5),
                               linewidth=0))

        q = np.array([[-size / 3], [-size / 3]])
        alfombra_sierpinski(ax, p + q, n - 1, size / 3)
        q = np.array([[-size / 3], [0]])
        alfombra_sierpinski(ax, p + q, n - 1, size / 3)
        q = np.array([[-size / 3], [size / 3]])
        alfombra_sierpinski(ax, p + q, n - 1, size / 3)

        q = np.array([[0], [-size / 3]])
        alfombra_sierpinski(ax, p + q, n - 1, size / 3)
        q = np.array([[0], [size / 3]])
        alfombra_sierpinski(ax, p + q, n - 1, size / 3)

        q = np.array([[size / 3], [-size / 3]])
        alfombra_sierpinski(ax, p + q, n - 1, size / 3)
        q = np.array([[size / 3], [0]])
        alfombra_sierpinski(ax, p + q, n - 1, size / 3)
        q = np.array([[size / 3], [size / 3]])
        alfombra_sierpinski(ax, p + q, n - 1, size / 3)


fig = plt.figure()
fig.patch.set_facecolor('white')
ax = plt.gca()
p = np.array([[0], [0]])
alfombra_sierpinski(ax, p, 4, 1)
ax.add_patch(Rectangle((-1 / 2, -1 / 2), 1, 1,
                       fill=False, edgecolor=(0, 0, 0),
                       linewidth=0.5))
plt.axis('equal')
plt.axis('off')
plt.show()
