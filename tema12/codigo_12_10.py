__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def sudoku_todas_sols(fila, col, S):
    # Comprueba si el Sudoku está completoe
    if fila == 9:
        imprime_sudoku(S)  # Imprime el Sudoku
        print()
    else:
        # Comprueba si el dígito en S[fila][col] es uno de los símbolos fijos iniciales
        if S[fila][col] != 0:

            # avanza a una nueva celda por filas de izquierda a derecha
            (new_fila, new_col) = avanza(fila, col)

            # Intenta expandir la solución parcial
            sudoku_todas_sols(new_fila, new_col, S)
        else:
            # Genera dígitos candidatos
            for k in range(1, 10):

                # Comprueba si el dígito k es un candidato válido
                if es_candidato_valido(fila, col, k, S):

                    # Include dígito en celda (fila,col)
                    S[fila][col] = k

                    # avanza a una nueva celda por filas de izquierda a derecha
                    (new_fila, new_col) = avanza(fila, col)

                    # Intenta expandir la solución parcial
                    sudoku_todas_sols(new_fila, new_col, S)

            # Celda vacía
            S[fila][col] = 0


# Calcula la nueva celda avanzado por filas de izquierda a derecha
def avanza(fila, col):
    if col == 8:
        return (fila + 1, 0)
    else:
        return (fila, col + 1)


# Test
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
