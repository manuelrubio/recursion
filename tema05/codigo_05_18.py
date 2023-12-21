__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def mcd1(m, n):
    if m == 0:
        return n
    elif m > n:
        return mcd1(n, m)
    else:
        return mcd1(m, n - m)


# Test
print(mcd1(0, 24))
print(mcd1(20, 0))
print(mcd1(20, 1))
print(mcd1(20, 3))
print(mcd1(20, 5))
print(mcd1(20, 10))
print(mcd1(20, 24))
