__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return suma_digitos(n // 10) + (n % 10)


def cuenta_digitos(n):
    if n == 0:
        return 0
    else:
        return cuenta_digitos(n // 10) + 1
