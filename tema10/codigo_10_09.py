__copyright__ = "Copyright (C) 2023 Manuel Rubio S�nchez"
__license__ = "MIT License"

def cuenta_pares_consecutivos(a):
    if len(a) == 2:
        return int(a[0] == a[1])
    else:
        return int(a[0] == a[1]) + cuenta_pares_consecutivos(a[1:])
