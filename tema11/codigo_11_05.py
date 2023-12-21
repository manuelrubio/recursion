__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def decimal_a_base_iterativo(n, b):
    s = 0
    p = 1
    while n > 0:
        s = s + (n % b) * p
        p = p * 10
        n = n // b
    return s


# Test
def decimal_a_base(n, b):
    if n < b:
        return n
    else:
        return 10 * decimal_a_base(n // b, b) + (n % b)


print(decimal_a_base_iterativo(0, 5))
print(decimal_a_base(0, 5))
print()

print(decimal_a_base_iterativo(3, 5))
print(decimal_a_base(3, 5))
print()

print(decimal_a_base_iterativo(5, 5))
print(decimal_a_base(5, 5))
print()

print(decimal_a_base_iterativo(15, 5))
print(decimal_a_base(15, 5))
print()

print(decimal_a_base_iterativo(35, 5))
print(decimal_a_base(35, 5))
print()

print(decimal_a_base_iterativo(142, 5))
print(decimal_a_base(142, 5))
print()
