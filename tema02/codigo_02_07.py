__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def suma_naturales_3(n):
    if n == 1:
        return 1
    else:
        return 2 * suma_naturales_3(n / 2) + (n / 2)**2

