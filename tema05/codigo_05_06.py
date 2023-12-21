__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def busqueda_lineal_rec_lineal(a, x, n):
    if a == []:
        return -n - 1
    elif a[0] == x:
        return 0
    else:
        return 1 + busqueda_lineal_rec_lineal(a[1:], x, n)


def busqueda_lineal_rec_lineal_wrapper(a, x):
    return busqueda_lineal_rec_lineal(a, x, len(a))


# Test
a = []
print(busqueda_lineal_rec_lineal_wrapper(a, 3))
print()

a = [2]
print(busqueda_lineal_rec_lineal_wrapper(a, 2))
print(busqueda_lineal_rec_lineal_wrapper(a, 8))
print()

a = [2, 4]
print(busqueda_lineal_rec_lineal_wrapper(a, 1))
print(busqueda_lineal_rec_lineal_wrapper(a, 2))
print(busqueda_lineal_rec_lineal_wrapper(a, 3))
print(busqueda_lineal_rec_lineal_wrapper(a, 4))
print(busqueda_lineal_rec_lineal_wrapper(a, 5))
print()

a = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(busqueda_lineal_rec_lineal_wrapper(a, 3))
print(busqueda_lineal_rec_lineal_wrapper(a, 0))
print(busqueda_lineal_rec_lineal_wrapper(a, 1))
print(busqueda_lineal_rec_lineal_wrapper(a, 2))
print(busqueda_lineal_rec_lineal_wrapper(a, 8))
print(busqueda_lineal_rec_lineal_wrapper(a, 13))
print(busqueda_lineal_rec_lineal_wrapper(a, 17))
print(busqueda_lineal_rec_lineal_wrapper(a, 19))
print(busqueda_lineal_rec_lineal_wrapper(a, 32))
print(busqueda_lineal_rec_lineal_wrapper(a, 42))
print(busqueda_lineal_rec_lineal_wrapper(a, 20))
