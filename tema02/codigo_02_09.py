__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def suma_naturales_5(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 2 * suma_naturales_5(n // 2) + (n // 2)**2
    else:
        return (2 * suma_naturales_5((n - 1) // 2)
                + ((n + 1) // 2)**2)


# Prueba
for n in range(1, 11):
    print(suma_naturales_5(n), n * (n + 1) // 2)
