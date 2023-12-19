def decimal_to_base(n, b):
    if n < b:
        return n
    else:
        return 10 * decimal_to_base(n // b, b) + (n % b)


# Test
print(decimal_to_base(142, 5))
print(decimal_to_base(0, 5))
print(decimal_to_base(3, 5))
print(decimal_to_base(5, 5))
print(decimal_to_base(15, 5))
print(decimal_to_base(35, 5))
