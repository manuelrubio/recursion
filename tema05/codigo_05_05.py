__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def busqueda_lineal_rec_por_cola(a, x):
    n = len(a)
    if a == []:
        return -1
    elif a[n - 1] == x:
        return n - 1
    else:
        return busqueda_lineal_rec_por_cola(a[:n - 1], x)


# Test
a = []
print(busqueda_lineal_rec_por_cola(a, 3))
print()

a = [2]
print(busqueda_lineal_rec_por_cola(a, 2))
print(busqueda_lineal_rec_por_cola(a, 8))
print()

a = [2, 4]
print(busqueda_lineal_rec_por_cola(a, 1))
print(busqueda_lineal_rec_por_cola(a, 2))
print(busqueda_lineal_rec_por_cola(a, 3))
print(busqueda_lineal_rec_por_cola(a, 4))
print(busqueda_lineal_rec_por_cola(a, 5))
print()

a = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(busqueda_lineal_rec_por_cola(a, 3))
print(busqueda_lineal_rec_por_cola(a, 0))
print(busqueda_lineal_rec_por_cola(a, 1))
print(busqueda_lineal_rec_por_cola(a, 2))
print(busqueda_lineal_rec_por_cola(a, 8))
print(busqueda_lineal_rec_por_cola(a, 13))
print(busqueda_lineal_rec_por_cola(a, 17))
print(busqueda_lineal_rec_por_cola(a, 19))
print(busqueda_lineal_rec_por_cola(a, 32))
print(busqueda_lineal_rec_por_cola(a, 42))
print(busqueda_lineal_rec_por_cola(a, 20))
