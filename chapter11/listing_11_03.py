def factorial_iterative(n):
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
    print(factorial_iterative(n))
    print(factorial(n))
    print()
