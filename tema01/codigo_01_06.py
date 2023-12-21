__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

# Decomposición: s(a) => s(a[0:n-1]), a[n-1]
def suma_lista_limites_1(a, inf, sup):
    if inf > sup:
        return 0
    else:
        return a[sup] + suma_lista_limites_1(a, inf, sup - 1)


# Decomposición: s(a) => a[0], s(a[1:n])
def suma_lista_limites_2(a, inf, sup):
    if inf > sup:
        return 0
    else:
        return a[inf] + suma_lista_limites_2(a, inf + 1, sup)


# Decomposición: s(a) => s(a[0:n//2]), s(a[n//2:n])
def suma_lista_limites_3(a, inf, sup):
    if inf > sup:
        return 0
    elif inf == sup:
        return a[inf]  # or a[sup]
    else:
        mitad = (sup + inf) // 2
        return (suma_lista_limites_3(a, inf, mitad)
                + suma_lista_limites_3(a, mitad + 1, sup))


# Una list:
a = [5, -1, 3, 2, 4, -3]

# Llamadas a las funciones:
print(suma_lista_limites_1(a, 0, len(a) - 1))
print(suma_lista_limites_2(a, 0, len(a) - 1))
print(suma_lista_limites_3(a, 0, len(a) - 1))
