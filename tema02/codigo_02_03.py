__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def escribe_digitos_invertidos_vertical(n):
    if n < 10:
        print(n)
    else:
        print(n % 10)
        escribe_digitos_invertidos_vertical(n // 10)


# Test
escribe_digitos_invertidos_vertical(0)
print()
escribe_digitos_invertidos_vertical(5)
print()
escribe_digitos_invertidos_vertical(24)
print()
escribe_digitos_invertidos_vertical(2743)
print()
