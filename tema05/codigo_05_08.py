__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def busqueda_binaria(a, x, inf, sup):
    if inf > sup:  # lista vacía
        return -1
    else:
        mitad = (inf + sup) // 2

        if x == a[mitad]:
            return mitad
        elif x < a[mitad]:
            return busqueda_binaria(a, x, inf, mitad - 1)
        else:
            return busqueda_binaria(a, x, mitad + 1, sup)


def busqueda_binaria_wrapper(a, x):
    return busqueda_binaria(a, x, 0, len(a) - 1)


# Test
a = []
print(busqueda_binaria_wrapper(a, 3))
print()

a = [2]
print(busqueda_binaria_wrapper(a, 2))
print(busqueda_binaria_wrapper(a, 8))
print()

a = [2, 4]
print(busqueda_binaria_wrapper(a, 1))
print(busqueda_binaria_wrapper(a, 2))
print(busqueda_binaria_wrapper(a, 3))
print(busqueda_binaria_wrapper(a, 4))
print(busqueda_binaria_wrapper(a, 5))
print()

a = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(busqueda_binaria_wrapper(a, 3))
print(busqueda_binaria_wrapper(a, 0))
print(busqueda_binaria_wrapper(a, 1))
print(busqueda_binaria_wrapper(a, 2))
print(busqueda_binaria_wrapper(a, 8))
print(busqueda_binaria_wrapper(a, 13))
print(busqueda_binaria_wrapper(a, 17))
print(busqueda_binaria_wrapper(a, 19))
print(busqueda_binaria_wrapper(a, 32))
print(busqueda_binaria_wrapper(a, 42))
print(busqueda_binaria_wrapper(a, 20))
