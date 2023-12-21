__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def maximo_lista_DyV(a):
    if len(a) == 1:
        return a[0]
    else:
        mitad = len(a) // 2
        m1 = maximo_lista_DyV(a[:mitad])
        m2 = maximo_lista_DyV(a[mitad:])
        return max(m1, m2)


def maximo_lista_limites_DyV(a, inf, sup):
    if inf == sup:
        return a[inf]  # o a[sup]
    else:
        mitad = (inf + sup) // 2
        m1 = maximo_lista_limites_DyV(a, inf, mitad)
        m2 = maximo_lista_limites_DyV(a, mitad + 1, sup)
        return max(m1, m2)


# Una lista:
v = [5, -1, 3, 2, 4, 7, 2]

# Llamadas a las funciones:
print(maximo_lista_DyV(v))
print(maximo_lista_limites_DyV(v, 0, len(v) - 1))
