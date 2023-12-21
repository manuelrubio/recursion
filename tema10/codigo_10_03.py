__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

import os


def imprime_ruta_fichero_iterativo(nombre_fichero, carpeta):
    pila = []
    for entrada in os.scandir(carpeta):
        if entrada.is_file() and nombre_fichero == entrada.name:
            print(entrada.path)
        elif entrada.is_dir():
            pila.append(entrada)

    while len(pila) > 0:
        entrada = pila.pop()
        for entrada in os.scandir(entrada.path):
            if entrada.is_file() and nombre_fichero == entrada.name:
                print(entrada.path)
            elif entrada.is_dir():
                pila.append(entrada)


imprime_ruta_fichero_iterativo('file01.txt', '.')
