__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def potencia_alt(b, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return potencia_alt(b, n // 2) * potencia_alt(b, n // 2)
    else:
        return (potencia_alt(b, (n - 1) // 2)
                * potencia_alt(b, (n - 1) // 2) * b)


# Test
print(potencia_alt(2, 0))
print(potencia_alt(2, 1))
print(potencia_alt(2, 4))
print(potencia_alt(2, 10))
