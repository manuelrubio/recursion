def power_general_linear(b, n):
    if n == 0:
        return 1
    elif n > 0:
        return b * power_general_linear(b, n - 1)
    else:
        return power_general_linear(b, n + 1) / b


# Test
print(power_general_linear(2, 0))
print(power_general_linear(2, 1))
print(power_general_linear(2, 4))
print(power_general_linear(2, 10))
print(power_general_linear(2, -1))
print(power_general_linear(2, -4))
print(power_general_linear(2, -10))
