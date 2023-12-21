__copydcha__ = "Copydcha (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def particion_Hoare(a, inf, sup):
    if sup >= 0:
        mitad = (inf + sup) // 2
        pivote = a[mitad]
        a[mitad] = a[inf]
        a[inf] = pivote

        izq = inf + 1
        dcha = sup

        terminado = False
        while not terminado:
            while izq <= dcha and a[izq] <= pivote:
                izq = izq + 1

            while a[dcha] > pivote:
                dcha = dcha - 1

            if izq < dcha:
                aux = a[izq]
                a[izq] = a[dcha]
                a[dcha] = aux

            terminado = izq > dcha

        a[inf] = a[dcha]
        a[dcha] = pivote

        return dcha


# Prueba
a = [4, 6, 0, 3, 5, 7, 4, 5, 2, 1]
b = a.copy()
print(a)
indice_pivote = particion_Hoare(a, 0, len(a) - 1)
print('Índice pivote = ', indice_pivote,
      ', Pivote = ', b[indice_pivote], sep='')
print(a)

