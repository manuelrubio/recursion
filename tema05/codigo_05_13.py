__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def particion_Hoare_rec(a, izq, dcha, pivote):
    if izq > dcha:
        return dcha
    else:
        if a[izq] > pivote and a[dcha] <= pivote:
            aux = a[izq]
            a[izq] = a[dcha]
            a[dcha] = aux
            return particion_Hoare_rec(a, izq + 1, dcha - 1, pivote)
        else:
            if a[izq] <= pivote:
                izq = izq + 1
            if a[dcha] > pivote:
                dcha = dcha - 1
            return particion_Hoare_rec(a, izq, dcha, pivote)


def particion_Hoare_wrapper(a, inf, sup):
    if sup >= 0:
        mitad = (inf + sup) // 2
        pivote = a[mitad]
        a[mitad] = a[inf]
        a[inf] = pivote

        dcha = particion_Hoare_rec(a, inf + 1, sup, pivote)

        a[inf] = a[dcha]
        a[dcha] = pivote

        return dcha


# Prueba
a = [4, 6, 0, 3, 5, 7, 4, 5, 2, 1]
b = a.copy()
print(a)
indice_pivote = particion_Hoare_wrapper(a, 0, len(a) - 1)
print('Índice pivote = ', indice_pivote,
      ', Pivote = ', b[indice_pivote], sep='')
print(a)
