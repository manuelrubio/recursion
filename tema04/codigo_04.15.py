__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def horner(c, x):
    if len(c) == 1:
        return c[0]
    else:
        return c[0] + x * horner(c[1:], x)


# Prueba
print(horner([5], 3))
print(horner([2, -1], 3))
print(horner([1, 2, 1], 3))
