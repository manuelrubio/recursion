__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def decimal_a_base(n, b):
    if n < b:
        return n
    else:
        return 10 * decimal_a_base(n // b, b) + (n % b)


# Prueba
print(decimal_a_base(142, 5))
print(decimal_a_base(0, 5))
print(decimal_a_base(3, 5))
print(decimal_a_base(5, 5))
print(decimal_a_base(15, 5))
print(decimal_a_base(35, 5))
