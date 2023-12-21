__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

# Precondiciones: n>=m, n>=2, m>=2
def factor_primo_menor(n, m):
    if n % m == 0:
        return m
    else:
        return factor_primo_menor(n, m + 1)
