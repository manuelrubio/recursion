__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

import math


def producto_escalar(u, v):
    s = 0
    for i in range(0, len(u)):
        s = s + u[i] * v[i]
    return s


def norma_Euclidea(v):
    return math.sqrt(producto_escalar(v, v))


def coseno(u, v):
    return producto_escalar(u, v) / norma_Euclidea(u) / norma_Euclidea(v)


# Example
a = [2, 1, 1]
b = [1, 0, 1]
print(coseno(a, b))
