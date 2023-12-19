def power_alt(b, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power_alt(b, n // 2) * power_alt(b, n // 2)
    else:
        return (power_alt(b, (n - 1) // 2)
                * power_alt(b, (n - 1) // 2) * b)


# Test
print(power_alt(2, 0))
print(power_alt(2, 1))
print(power_alt(2, 4))
print(power_alt(2, 10))
