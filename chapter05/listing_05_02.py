def contains_digit_tail(n, d):
    if n < 10:
        return n == d
    elif n % 10 == d:
        return True
    else:
        return contains_digit_tail(n // 10, d)


# Test
print(contains_digit_tail(0, 3))
print(contains_digit_tail(2, 3))
print(contains_digit_tail(3, 3))
print(contains_digit_tail(12, 3))
print(contains_digit_tail(13, 3))
print(contains_digit_tail(35, 3))
print(contains_digit_tail(33, 3))
print(contains_digit_tail(19862, 3))
print(contains_digit_tail(19863, 3))
print(contains_digit_tail(19832, 3))
print(contains_digit_tail(39812, 3))
print(contains_digit_tail(33333, 3))
