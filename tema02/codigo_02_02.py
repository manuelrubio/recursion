__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return suma_digitos(n // 10) + (n % 10)


# Prueba
print(suma_digitos(0))
print(suma_digitos(5))
print(suma_digitos(29))
print(suma_digitos(5342))
print(suma_digitos(879))
