def add_digits(n):
    if n < 10:
        return n
    else:
        return add_digits(n // 10) + (n % 10)


# Test
print(add_digits(0))
print(add_digits(5))
print(add_digits(29))
print(add_digits(5342))
print(add_digits(879))
