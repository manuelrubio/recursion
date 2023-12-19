def contains_digit(n, d):
    if n < 10:
        return n == d
    else:
        return (n % 10 == d) or contains_digit(n // 10, d)


# Test
print(contains_digit(0, 3))
print(contains_digit(2, 3))
print(contains_digit(3, 3))
print(contains_digit(12, 3))
print(contains_digit(13, 3))
print(contains_digit(35, 3))
print(contains_digit(33, 3))
print(contains_digit(19862, 3))
print(contains_digit(19863, 3))
print(contains_digit(19832, 3))
print(contains_digit(39812, 3))
print(contains_digit(33333, 3))
