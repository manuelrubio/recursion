def factorial_tail(n, p):
    if n == 0:
        return p
    else:
        return factorial_tail(n - 1, p * n)


def factorial_tail_recursive_wrapper(n):
    return factorial_tail(n, 1)


# Test
def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n


for n in range(0, 11):
    print(factorial_tail_recursive_wrapper(n))
    print(factorial(n))
    print()
