__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def factorial_por_cola(n, p):
    if n == 0:
        return p
    else:
        return factorial_por_cola(n - 1, p * n)


def factorial_por_cola_wrapper(n):
    return factorial_por_cola(n, 1)


# Test
def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n


for n in range(0, 11):
    print(factorial_por_cola_wrapper(n))
    print(factorial(n))
    print()
