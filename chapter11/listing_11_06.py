def decimal_to_base_tail(n, b, p, s):
    if n == 0:
        return s
    else:
        return decimal_to_base_tail(n // b, b, 10 * p,
                                    s + (n % b) * p)


def decimal_to_base_tail_wrapper(n, b):
    return decimal_to_base_tail(n, b, 1, 0)


# Test
def decimal_to_base(n, b):
    if n < b:
        return n
    else:
        return 10 * decimal_to_base(n // b, b) + (n % b)


print(decimal_to_base_tail_wrapper(0, 5))
print(decimal_to_base(0, 5))
print()

print(decimal_to_base_tail_wrapper(3, 5))
print(decimal_to_base(3, 5))
print()

print(decimal_to_base_tail_wrapper(5, 5))
print(decimal_to_base(5, 5))
print()

print(decimal_to_base_tail_wrapper(15, 5))
print(decimal_to_base(15, 5))
print()

print(decimal_to_base_tail_wrapper(35, 5))
print(decimal_to_base(35, 5))
print()

print(decimal_to_base_tail_wrapper(142, 5))
print(decimal_to_base(142, 5))
print()
