__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

import os


def imprime_ruta_fichero_recursivo(nombre_fichero, carpeta):
    for entrada in os.scandir(carpeta):
        if entrada.is_file() and nombre_fichero == entrada.name:
            print(entrada.path)
        elif entrada.is_dir():
            imprime_ruta_fichero_recursivo(nombre_fichero, entrada.path)


imprime_ruta_fichero_recursivo('file01.txt', '.')
