def gcd1_iterative(m, n):
    while m > 0:
        if m > n:
            aux = n
            n = m
            m = aux
        else:
            n = n - m

    return n


# Test
def gcd1(m, n):
    if m == 0:
        return n
    elif m > n:
        return gcd1(n, m)
    else:
        return gcd1(m, n - m)


# Test
print(gcd1_iterative(0, 24), ' = ', gcd1(0, 24))
print(gcd1_iterative(20, 0), ' = ', gcd1(20, 0))
print(gcd1_iterative(20, 1), ' = ', gcd1(20, 1))
print(gcd1_iterative(20, 3), ' = ', gcd1(20, 3))
print(gcd1_iterative(20, 5), ' = ', gcd1(20, 5))
print(gcd1_iterative(20, 10), ' = ', gcd1(20, 10))
print(gcd1_iterative(20, 24), ' = ', gcd1(20, 24))
