__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def adultos(n):
    if n == 1:
        return 0
    else:
        return adultos(n - 1) + bebes(n - 1)


def bebes(n):
    if n == 1:
        return 1
    else:
        return adultos(n - 1)


# Test
import math

phi = (1 + math.sqrt(5)) / 2


def fib(n):
    if (n == 1) or (n == 2):
        return 1
    else:
        return math.floor(phi * fib(n - 1) + 0.5)


for n in range(1, 11):
    print('{0:4}'.format(bebes(n)), sep=' ', end='')

print()
for n in range(1, 11):
    print('{0:4}'.format(adultos(n)), sep=' ', end='')

print()
for n in range(1, 11):
    print('{0:4}'.format(fib(n)), sep=' ', end='')
