__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n


def factorial_redundante(n):
    if n == 0 or n == 1:
        return 1
    else:
        return factorial_redundante(n - 1) * n


def factorial_sin_caso_base(n):
    if n == 1:
        return 1
    else:
        return factorial_sin_caso_base(n - 1) * n


def factorial_sin_casos_base(n):
    return factorial_sin_casos_base(n - 1) * n


# Prueba
import math

for n in range(0, 20):
    print(factorial(n), math.factorial(n))
