__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

# Decomposición: s(a) => s(a[0:n-1]), a[n-1]
def suma_lista_1(a):
    if len(a) == 0:
        return 0
    else:
        return (suma_lista_1(a[0:len(a) - 1]) + a[len(a) - 1])


# Decomposición: s(a) => a[0], s(a[1:n])
def suma_lista_2(a):
    if len(a) == 0:
        return 0
    else:
        return a[0] + suma_lista_2(a[1:len(a)])


# Decomposición: s(a) => s(a[0:n//2]), s(a[n//2:n])
def suma_lista_3(a):
    if len(a) == 0:
        return 0
    elif len(a) == 1:
        return a[0]
    else:
        mitad = len(a) // 2
        return (suma_lista_3(a[0:mitad])
                + suma_lista_3(a[mitad:len(a)]))


# Una lista:
a = [5, -1, 3, 2, 4, -3]

# Llamadas a las funciones:
print(suma_lista_1(a))
print(suma_lista_2(a))
print(suma_lista_3(a))
