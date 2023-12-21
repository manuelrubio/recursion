__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def suma_lenta(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return suma_lenta(a - 1, b) + 1


# Test
print(suma_lenta(0, 0))
print(suma_lenta(0, 6))
print(suma_lenta(13, 0))
print(suma_lenta(4, 32))
