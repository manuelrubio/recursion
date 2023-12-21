__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def suma_lenta_mas_rapida_alt(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return suma_lenta_mas_rapida_alt(a - 1, b - 1) + 1 + 1


# Test
print(suma_lenta_mas_rapida_alt(0, 0))
print(suma_lenta_mas_rapida_alt(0, 6))
print(suma_lenta_mas_rapida_alt(13, 0))
print(suma_lenta_mas_rapida_alt(4, 32))
