__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def circuito(n, r):
    if n == 1:
        return r
    else:
        return 1 / (1 / r + 1 / (circuito(n - 1, r) + r))


# Prueba
import math
import random

phi = (1 + math.sqrt(5)) / 2


def fib(n):
    if (n == 1) or (n == 2):
        return 1
    else:
        return math.floor(phi * fib(n - 1) + 0.5)


for i in range(1, 11):
    r = random.random()
    n = random.randint(1, 10)
    print(circuito(n, r), '=', r * fib(2 * n - 1) / fib(2 * n))
