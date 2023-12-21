__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def potencia_lineal(b, n):
    if n == 0:
        return 1
    else:
        return b * potencia_lineal(b, n - 1)


# Pruebas
print(potencia_lineal(2, 0))
print(potencia_lineal(2, 1))
print(potencia_lineal(2, 4))
print(potencia_lineal(2, 10))
