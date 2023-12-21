__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def longitud_subsecuencia_capicua_mas_larga(a):
    n = len(a)
    if n <= 1:
        return n
    else:
        if a[0] == a[n - 1]:
            return 2 + longitud_subsecuencia_capicua_mas_larga(
                a[1:n - 1])
        else:
            l1 = longitud_subsecuencia_capicua_mas_larga(a[1:n])
            l2 = longitud_subsecuencia_capicua_mas_larga(a[0:n - 1])
            return max(l1, l2)
