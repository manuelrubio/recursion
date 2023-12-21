__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def decimal_a_binario(n):
    if n < 2:
        return n
    else:
        return 10 * decimal_a_binario(n // 2) + (n % 2)


# Prueba
print(decimal_a_binario(0))
print(decimal_a_binario(1))
print(decimal_a_binario(2))
print(decimal_a_binario(3))
print(decimal_a_binario(4))
print(decimal_a_binario(23))
print(decimal_a_binario(142))
