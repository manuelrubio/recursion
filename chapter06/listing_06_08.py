def number_of_bits(n):
    if n < 2:
        return 1
    else:
        return 1 + number_of_bits(n >> 1)


def multiply_karatsuba(x, y):
    if x == 0 or y == 0:
        return 0
    elif x == 1:
        return y
    elif y == 1:
        return x
    else:
        n_bits_x = number_of_bits(x)
        n_bits_y = number_of_bits(y)

        m = min(n_bits_x // 2, n_bits_y // 2)

        a = x >> m
        b = x - (a << m)
        c = y >> m
        d = y - (c << m)

        ac = multiply_karatsuba(a, c)
        bd = multiply_karatsuba(b, d)
        t = multiply_karatsuba(a + b, c + d) - ac - bd

        return (ac << (2 * m)) + (t << m) + bd


# Test
print(multiply_karatsuba(0, 0))
print(multiply_karatsuba(0, 5))
print(multiply_karatsuba(3, 0))
print(multiply_karatsuba(1, 5))
print(multiply_karatsuba(3, 1))
print(multiply_karatsuba(3, 5))
print(multiply_karatsuba(11, 15))
print(multiply_karatsuba(324, 125))
