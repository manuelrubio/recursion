__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def suma_naturales(n):
    if n == 1:
        return 1  # Caso base
    else:
        return suma_naturales(n - 1) + n  # Caso recursivo


# Prueba
for n in range(1, 11):
    print(suma_naturales(n), n * (n + 1) // 2)
