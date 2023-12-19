def slow_addition(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return slow_addition(a - 1, b) + 1


# Test
print(slow_addition(0, 0))
print(slow_addition(0, 6))
print(slow_addition(13, 0))
print(slow_addition(4, 32))
