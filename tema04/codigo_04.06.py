__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def suma_lenta_mas_rapida(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a < b:
        return suma_lenta_mas_rapida(a - 1, b) + 1
    else:
        return suma_lenta_mas_rapida(a, b - 1) + 1


# Test
print(suma_lenta_mas_rapida(0, 0))
print(suma_lenta_mas_rapida(0, 6))
print(suma_lenta_mas_rapida(13, 0))
print(suma_lenta_mas_rapida(4, 32))
