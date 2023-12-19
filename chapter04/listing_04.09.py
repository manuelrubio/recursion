def decimal_to_binary(n):
    if n < 2:
        return n
    else:
        return 10 * decimal_to_binary(n // 2) + (n % 2)


# Test
print(decimal_to_binary(0))
print(decimal_to_binary(1))
print(decimal_to_binary(2))
print(decimal_to_binary(3))
print(decimal_to_binary(4))
print(decimal_to_binary(23))
print(decimal_to_binary(142))
