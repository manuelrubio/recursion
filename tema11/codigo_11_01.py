__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def mcd1_iterativo(m, n):
    while m > 0:
        if m > n:
            aux = n
            n = m
            m = aux
        else:
            n = n - m

    return n


# Test
def mcd1(m, n):
    if m == 0:
        return n
    elif m > n:
        return mcd1(n, m)
    else:
        return mcd1(m, n - m)


# Test
print(mcd1_iterativo(0, 24), ' = ', mcd1(0, 24))
print(mcd1_iterativo(20, 0), ' = ', mcd1(20, 0))
print(mcd1_iterativo(20, 1), ' = ', mcd1(20, 1))
print(mcd1_iterativo(20, 3), ' = ', mcd1(20, 3))
print(mcd1_iterativo(20, 5), ' = ', mcd1(20, 5))
print(mcd1_iterativo(20, 10), ' = ', mcd1(20, 10))
print(mcd1_iterativo(20, 24), ' = ', mcd1(20, 24))
