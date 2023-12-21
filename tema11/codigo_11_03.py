__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def factorial_iterativo(n):
    p = 1
    while n > 0:
        p = p * n
        n = n - 1

    return p


# Test
def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n


for n in range(0, 11):
    print(factorial_iterativo(n))
    print(factorial(n))
    print()
