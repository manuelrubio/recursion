__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def potencia_general_lineal(b, n):
    if n == 0:
        return 1
    elif n > 0:
        return b * potencia_general_lineal(b, n - 1)
    else:
        return potencia_general_lineal(b, n + 1) / b


# Test
print(potencia_general_lineal(2, 0))
print(potencia_general_lineal(2, 1))
print(potencia_general_lineal(2, 4))
print(potencia_general_lineal(2, 10))
print(potencia_general_lineal(2, -1))
print(potencia_general_lineal(2, -4))
print(potencia_general_lineal(2, -10))
