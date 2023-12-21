__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def es_par_correcto(n):
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return es_par_correcto(n - 2)


# Test
for n in range(0, 10):
    print(n, ' es par: ', es_par_correcto(n), sep='')
