def horner(c, x):
    if len(c) == 1:
        return c[0]
    else:
        return c[0] + x * horner(c[1:], x)


# Test
print(horner([5], 3))
print(horner([2, -1], 3))
print(horner([1, 2, 1], 3))
