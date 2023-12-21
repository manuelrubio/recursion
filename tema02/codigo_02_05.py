__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def es_par_incorrecto(n):
    if n == 0:
        return True
    else:
        return es_par_incorrecto(n - 2)


# Prueba
print(es_par_incorrecto(4))
print(es_par_incorrecto(0))

# Error: maximum recursion depth exceeded in comparison
print(es_par_incorrecto(7))
