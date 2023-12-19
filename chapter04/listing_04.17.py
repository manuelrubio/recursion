def circuit(n, r):
    if n == 1:
        return r
    else:
        return 1 / (1 / r + 1 / (circuit(n - 1, r) + r))


# Test
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
    print(circuit(n, r), '=', r * fib(2 * n - 1) / fib(2 * n))
