__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def potencia_logaritmica(b, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return potencia_logaritmica(b, n // 2)**2
    else:
        return b * (potencia_logaritmica(b, (n - 1) // 2)**2)


# Test
print(potencia_logaritmica(2, 0))
print(potencia_logaritmica(2, 1))
print(potencia_logaritmica(2, 4))
print(potencia_logaritmica(2, 10))
