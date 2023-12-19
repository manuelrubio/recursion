def fibonacci_alt(n):
    if n == 1 or n == 2:
        return 1
    else:
        aux = 1
        for i in range(1, n - 1):
            aux += fibonacci_alt(i)
        return aux


# Test
for n in range(1, 11):
    print(fibonacci_alt(n))
