__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def decimal_a_base_por_cola(n, b, p, s):
    if n == 0:
        return s
    else:
        return decimal_a_base_por_cola(n // b, b, 10 * p,
                                    s + (n % b) * p)


def decimal_a_base_por_cola_wrapper(n, b):
    return decimal_a_base_por_cola(n, b, 1, 0)


# Test
def decimal_a_base(n, b):
    if n < b:
        return n
    else:
        return 10 * decimal_a_base(n // b, b) + (n % b)


print(decimal_a_base_por_cola_wrapper(0, 5))
print(decimal_a_base(0, 5))
print()

print(decimal_a_base_por_cola_wrapper(3, 5))
print(decimal_a_base(3, 5))
print()

print(decimal_a_base_por_cola_wrapper(5, 5))
print(decimal_a_base(5, 5))
print()

print(decimal_a_base_por_cola_wrapper(15, 5))
print(decimal_a_base(15, 5))
print()

print(decimal_a_base_por_cola_wrapper(35, 5))
print(decimal_a_base(35, 5))
print()

print(decimal_a_base_por_cola_wrapper(142, 5))
print(decimal_a_base(142, 5))
print()
