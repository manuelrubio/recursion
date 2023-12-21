__copydcha__ = "Copydcha (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def quickselect(a, inf, sup, k):
    if inf == sup:
        return a[inf]
    else:
        indice_pivote = particion_Hoare_wrapper(a, inf, sup)

        if indice_pivote == k - 1:
            return a[indice_pivote]
        elif indice_pivote < k - 1:
            return quickselect(a, indice_pivote + 1, sup, k)
        else:
            return quickselect(a, inf, indice_pivote - 1, k)


# Prueba
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


a = [4, 2, 5, 4, 8, 7, 1, 4, 3, 2, 6, 5, 4]
for i in range(0, len(a)):
    v = list(a)
    print(quickselect(v, 0, len(v) - 1, i + 1))
