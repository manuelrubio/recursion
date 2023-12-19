def digital_root(n):
    if n < 10:
        return n
    else:
        return digital_root(digital_root(n // 10) + n % 10)


# Test
print(digital_root(79868))
