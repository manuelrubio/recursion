def gcd1(m, n):
    if m == 0:
        return n
    elif m > n:
        return gcd1(n, m)
    else:
        return gcd1(m, n - m)


# Test
print(gcd1(0, 24))
print(gcd1(20, 0))
print(gcd1(20, 1))
print(gcd1(20, 3))
print(gcd1(20, 5))
print(gcd1(20, 10))
print(gcd1(20, 24))
