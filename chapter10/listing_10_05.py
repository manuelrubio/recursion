def fib_memoization(n, a):
    if n == 1 or n == 2:
        return 1
    elif a[n] > 0:
        return a[n]
    else:
        a[n] = fib_memoization(
            n - 1, a) + fib_memoization(n - 2, a)
        return a[n]


n = 100
print(fib_memoization(n, [0] * (n + 1)))
