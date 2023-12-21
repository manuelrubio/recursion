__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def agua_rec_multiple(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return 3 * agua_rec_multiple(n - 1) - agua_rec_multiple(n - 2)


# Prueba
import math

phi = (1 + math.sqrt(5)) / 2


def fib(n):
    if (n == 1) or (n == 2):
        return 1
    else:
        return math.floor(phi * fib(n - 1) + 0.5)


for n in range(1, 11):
    print('{0:6}'.format(agua_rec_multiple(n)), sep=' ', end='')


print()
for n in range(1, 11):
    print('{0:6}'.format(fib(2 * n)), sep=' ', end='')
