def quicker_slow_addition(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a < b:
        return quicker_slow_addition(a - 1, b) + 1
    else:
        return quicker_slow_addition(a, b - 1) + 1


# Test
print(quicker_slow_addition(0, 0))
print(quicker_slow_addition(0, 6))
print(quicker_slow_addition(13, 0))
print(quicker_slow_addition(4, 32))
