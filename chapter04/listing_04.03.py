def power_logarithmic(b, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power_logarithmic(b, n // 2)**2
    else:
        return b * (power_logarithmic(b, (n - 1) // 2)**2)


# Test
print(power_logarithmic(2, 0))
print(power_logarithmic(2, 1))
print(power_logarithmic(2, 4))
print(power_logarithmic(2, 10))
