__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def fib_memoizacion(n, a):
    if n == 1 or n == 2:
        return 1
    elif a[n] > 0:
        return a[n]
    else:
        a[n] = fib_memoizacion(
            n - 1, a) + fib_memoizacion(n - 2, a)
        return a[n]


n = 100
print(fib_memoizacion(n, [0] * (n + 1)))
