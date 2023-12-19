def quicker_slow_addition_alt(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return quicker_slow_addition_alt(a - 1, b - 1) + 1 + 1


# Test
print(quicker_slow_addition_alt(0, 0))
print(quicker_slow_addition_alt(0, 6))
print(quicker_slow_addition_alt(13, 0))
print(quicker_slow_addition_alt(4, 32))
