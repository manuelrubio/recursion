__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def suma_naturales_2(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    elif n % 2:
        return (3 * suma_naturales_2((n - 1) / 2)
                + suma_naturales_2((n + 1) / 2))
    else:
        return (3 * suma_naturales_2(n / 2)
                + suma_naturales_2(n / 2 - 1))


# Prueba
for n in range(1, 11):
    print(suma_naturales_2(n), n * (n + 1) // 2)
