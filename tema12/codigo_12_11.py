__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

import math


# Comprueba si un dígito en la celda (fila,col) es válido
def es_candidato_valido(fila, col, digito, S):
    # Comprueba conflicto en fila
    for k in range(0, 9):
        if k != col and digito == S[fila][k]:
            return False

    # Comprueba conflicto en columna
    for k in range(0, 9):
        if k != fila and digito == S[k][col]:
            return False

    # Comprueba conflicto en caja
    fila_caja = math.floor(fila / 3)
    col_caja = math.floor(col / 3)
    for k in range(0, 3):
        for m in range(0, 3):
            if (fila != 3 * fila_caja + k
                    and col != 3 * col_caja + m):
                if digito == S[3 * fila_caja + k][3 * col_caja + m]:
                    return False

    return True


# Lee un Sudoku de un fichero de texto
def lee_sudoku(nombre_fichero):
    fichero = open(nombre_fichero, 'r')
    S = [[None] * 9] * 9
    i = 0
    for linea in fichero.readlines():
        S[i] = [int(x) for x in linea.split(' ')]
        i = i + 1

    fichero.close()
    return S


# Imprime un Sudoku en la consola
def imprime_sudoku(S):
    for s in S:
        print(*s)


S = lee_sudoku('sudoku01_input.txt')  # Algún fichero
sudoku_todas_sols(0, 0, S)