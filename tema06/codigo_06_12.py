__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

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
