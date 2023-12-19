def power_linear(b, n):
    if n == 0:
        return 1
    else:
        return b * power_linear(b, n - 1)


# Test
print(power_linear(2, 0))
print(power_linear(2, 1))
print(power_linear(2, 4))
print(power_linear(2, 10))
