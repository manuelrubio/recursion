def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n - 1)


def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n - 1)


# Test
for n in range(0, 6):
    print(is_even(n))

print()
for n in range(0, 6):
    print(is_odd(n))
