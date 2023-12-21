__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def quick_sort_inplace(a, inf, sup):
    if inf < sup:
        indice_pivote = particion_Hoare_wrapper(a, inf, sup)

        quick_sort_inplace(a, inf, indice_pivote - 1)
        quick_sort_inplace(a, indice_pivote + 1, sup)


# Test
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


a = []
print(a)
quick_sort_inplace(a, 0, len(a) - 1)
print(a)
print()

a = [5]
print(a)
quick_sort_inplace(a, 0, len(a) - 1)
print(a)
print()

a = [3, 5]
print(a)
quick_sort_inplace(a, 0, len(a) - 1)
print(a)
print()

a = [5, 3]
print(a)
quick_sort_inplace(a, 0, len(a) - 1)
print(a)
print()

a = [1, 3, 5]
print(a)
quick_sort_inplace(a, 0, len(a) - 1)
print(a)
print()

a = [1, 5, 3]
print(a)
quick_sort_inplace(a, 0, len(a) - 1)
print(a)
print()

a = [3, 1, 5]
print(a)
quick_sort_inplace(a, 0, len(a) - 1)
print(a)
print()

a = [3, 5, 1]
print(a)
quick_sort_inplace(a, 0, len(a) - 1)
print(a)
print()

a = [5, 1, 3]
print(a)
quick_sort_inplace(a, 0, len(a) - 1)
print(a)
print()

a = [5, 3, 1]
print(a)
quick_sort_inplace(a, 0, len(a) - 1)
print(a)
print()

a = [72, 28, 30, 80, 18, 94, 54, 95, 12, 6, 26, 43, 18]
print(a)
quick_sort_inplace(a, 0, len(a) - 1)
print(a)
print()
