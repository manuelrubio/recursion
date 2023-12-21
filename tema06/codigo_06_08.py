__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def numero_de_bits(n):
    if n < 2:
        return 1
    else:
        return 1 + numero_de_bits(n >> 1)


def multiplica_karatsuba(x, y):
    if x == 0 or y == 0:
        return 0
    elif x == 1:
        return y
    elif y == 1:
        return x
    else:
        n_bits_x = numero_de_bits(x)
        n_bits_y = numero_de_bits(y)

        m = min(n_bits_x // 2, n_bits_y // 2)

        a = x >> m
        b = x - (a << m)
        c = y >> m
        d = y - (c << m)

        ac = multiplica_karatsuba(a, c)
        bd = multiplica_karatsuba(b, d)
        t = multiplica_karatsuba(a + b, c + d) - ac - bd

        return (ac << (2 * m)) + (t << m) + bd


# Test
print(multiplica_karatsuba(0, 0))
print(multiplica_karatsuba(0, 5))
print(multiplica_karatsuba(3, 0))
print(multiplica_karatsuba(1, 5))
print(multiplica_karatsuba(3, 1))
print(multiplica_karatsuba(3, 5))
print(multiplica_karatsuba(11, 15))
print(multiplica_karatsuba(324, 125))
