def decimal_to_base_iterative(n, b):
    s = 0
    p = 1
    while n > 0:
        s = s + (n % b) * p
        p = p * 10
        n = n // b
    return s


# Test
def decimal_to_base(n, b):
    if n < b:
        return n
    else:
        return 10 * decimal_to_base(n // b, b) + (n % b)


print(decimal_to_base_iterative(0, 5))
print(decimal_to_base(0, 5))
print()

print(decimal_to_base_iterative(3, 5))
print(decimal_to_base(3, 5))
print()

print(decimal_to_base_iterative(5, 5))
print(decimal_to_base(5, 5))
print()

print(decimal_to_base_iterative(15, 5))
print(decimal_to_base(15, 5))
print()

print(decimal_to_base_iterative(35, 5))
print(decimal_to_base(35, 5))
print()

print(decimal_to_base_iterative(142, 5))
print(decimal_to_base(142, 5))
print()
