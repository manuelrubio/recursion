def water_multiple(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return 3 * water_multiple(n - 1) - water_multiple(n - 2)


# Test
import math

phi = (1 + math.sqrt(5)) / 2


def fib(n):
    if (n == 1) or (n == 2):
        return 1
    else:
        return math.floor(phi * fib(n - 1) + 0.5)


for n in range(1, 11):
    print('{0:6}'.format(water_multiple(n)), sep=' ', end='')


print()
for n in range(1, 11):
    print('{0:6}'.format(fib(2 * n)), sep=' ', end='')
