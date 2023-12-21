__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

import random
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def dibuja_L1(x, y):
    plt.plot([x, x + 2], [y + 2, y + 2], 'k-')
    plt.plot([x, x + 1], [y + 1, y + 1], 'k-')
    plt.plot([x + 1, x + 2], [y, y], 'k-')
    plt.plot([x, x], [y + 1, y + 2], 'k-')
    plt.plot([x + 1, x + 1], [y, y + 1], 'k-')
    plt.plot([x + 2, x + 2], [y, y + 2], 'k-')


def dibuja_L2(x, y):
    plt.plot([x, x + 2], [y + 2, y + 2], 'k-')
    plt.plot([x, x + 1], [y, y], 'k-')
    plt.plot([x + 1, x + 2], [y + 1, y + 1], 'k-')
    plt.plot([x, x], [y, y + 2], 'k-')
    plt.plot([x + 1, x + 1], [y, y + 1], 'k-')
    plt.plot([x + 2, x + 2], [y + 1, y + 2], 'k-')


def dibuja_L3(x, y):
    plt.plot([x, x + 2], [y, y], 'k-')
    plt.plot([x, x + 1], [y + 1, y + 1], 'k-')
    plt.plot([x + 1, x + 2], [y + 2, y + 2], 'k-')
    plt.plot([x, x], [y, y + 1], 'k-')
    plt.plot([x + 1, x + 1], [y + 1, y + 2], 'k-')
    plt.plot([x + 2, x + 2], [y, y + 2], 'k-')


def dibuja_L4(x, y):
    plt.plot([x, x + 2], [y, y], 'k-')
    plt.plot([x, x + 1], [y + 2, y + 2], 'k-')
    plt.plot([x + 1, x + 2], [y + 1, y + 1], 'k-')
    plt.plot([x, x], [y, y + 2], 'k-')
    plt.plot([x + 1, x + 1], [y + 1, y + 2], 'k-')
    plt.plot([x + 2, x + 2], [y, y + 1], 'k-')


def trominos(x, y, n, p, q):
    if n == 2:
        if y == q:  # agujero en teja inferior
            if x == p:  # agujero en teja inferior-izquierda
                dibuja_L1(x, y)
            else:  # agujero en teja inferior-derecha
                dibuja_L2(x, y)
        else:  # agujero en teja inferior
            if x == p:  # agujero en teja superior-izquierda
                dibuja_L3(x, y)
            else:  # agujero en teja superior-derecha
                dibuja_L4(x, y)
    else:
        mitad_x = x + n // 2
        mitad_y = y + n // 2
        if q < mitad_y:  # agujero en cuadrados inferiores
            if p < mitad_x:  # agujero en cuadrado inferior-izquierdo
                dibuja_L1(mitad_x - 1, mitad_y - 1)
                trominos(x, y, n // 2, p, q)
                trominos(x, mitad_y, n // 2, mitad_x - 1, mitad_y)
                trominos(mitad_x, y, n // 2, mitad_x, mitad_y - 1)
                trominos(mitad_x, mitad_y, n // 2, mitad_x, mitad_y)
            else:  # agujero en cuadrado inferior-derecho
                dibuja_L2(mitad_x - 1, mitad_y - 1)
                trominos(x, y, n // 2, mitad_x - 1, mitad_y - 1)
                trominos(x, mitad_y, n // 2, mitad_x - 1, mitad_y)
                trominos(mitad_x, y, n // 2, p, q)
                trominos(mitad_x, mitad_y, n // 2, mitad_x, mitad_y)
        else:  # agujero en cuadrados superiores
            if p < mitad_x:  # agujero en cuadrado superior-izquierdo
                dibuja_L3(mitad_x - 1, mitad_y - 1)
                trominos(x, y, n // 2, mitad_x - 1, mitad_y - 1)
                trominos(x, mitad_y, n // 2, p, q)
                trominos(mitad_x, y, n // 2, mitad_x, mitad_y - 1)
                trominos(mitad_x, mitad_y, n // 2, mitad_x, mitad_y)
            else:  # agujero en cuadrado superior-derecho
                dibuja_L4(mitad_x - 1, mitad_y - 1)
                trominos(x, y, n // 2, mitad_x - 1, mitad_y - 1)
                trominos(x, mitad_y, n // 2, mitad_x - 1, mitad_y)
                trominos(mitad_x, y, n // 2, mitad_x, mitad_y - 1)
                trominos(mitad_x, mitad_y, n // 2, p, q)


fig = plt.figure()
fig.patch.set_facecolor('white')
ax = plt.gca()
n = 16  # potencia de 2
p = random.choice([i for i in range(n)])
q = random.choice([i for i in range(n)])
ax.add_patch(Rectangle((p, q), 1, 1, facecolor=(0.5, 0.5, 0.5)))
trominos(0, 0, n, p, q)
plt.axis('equal')
plt.axis('off')
plt.show()
