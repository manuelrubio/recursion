def print_digits_reversed_vertically(n):
    if n < 10:
        print(n)
    else:
        print(n % 10)
        print_digits_reversed_vertically(n // 10)


# Test
print_digits_reversed_vertically(0)
print()
print_digits_reversed_vertically(5)
print()
print_digits_reversed_vertically(24)
print()
print_digits_reversed_vertically(2743)
print()
