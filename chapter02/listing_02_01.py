def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n


def factorial_redundant(n):
    if n == 0 or n == 1:
        return 1
    else:
        return factorial_redundant(n - 1) * n


def factorial_missing_base_case(n):
    if n == 1:
        return 1
    else:
        return factorial_missing_base_case(n - 1) * n


def factorial_no_base_case(n):
    return factorial_no_base_case(n - 1) * n


# Test
import math

for n in range(0, 20):
    print(factorial(n), math.factorial(n))
