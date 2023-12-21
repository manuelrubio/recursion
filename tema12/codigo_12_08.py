__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def busca_camino_laberinto(M, fila, col, incr, fila_salida, col_salida):
    # Caso base: comprueba si se ha encontrado un camino
    if fila == fila_salida and col == col_salida:
        return True  # Solución encontrada
    else:
        sol_encontrada = False
        # Genera candidatos
        k = 0
        while not sol_encontrada and k < 4:

            # Nueva celda candidata
            nueva_col = col + incr[k][0]
            nueva_fila = fila + incr[k][1]

            # Comprueba la validez de la nueva celda
            if (nueva_fila >= 0 and nueva_fila < len(M)
                    and nueva_col >= 0 and nueva_col < len(M[0])
                    and M[nueva_fila][nueva_col] == 'E'):

                # Añade la celda al camino (a la solución parcial)
                M[nueva_fila][nueva_col] = 'P'

                # Intenta extender el camino partiendo de la nueva celda
                sol_encontrada = busca_camino_laberinto(
                    M, nueva_fila, nueva_col, incr,
                    fila_salida, col_salida)

                # Marca la celda como vacía si no forma parte de la solución
                if not sol_encontrada:
                    M[nueva_fila][nueva_col] = 'E'

            k = k + 1

        return sol_encontrada


def busca_camino_laberinto_wrapper(M, fila_entrada, col_entrada,
                           fila_salida, col_salida):
    # Direcciones de búsqueda
    incr = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    M[fila_entrada][col_entrada] = 'P'
    return busca_camino_laberinto(M, fila_entrada, col_entrada, incr,
                          fila_salida, col_salida)


# Test
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def lee_laberinto_de_fichero(nombre_fichero):
    fichero = open(nombre_fichero, 'r')
    M = []
    for line in fichero.readlines():
        M.append([x[0] for x in line.split(' ')])
    fichero.close()
    return M


gris = (0.75, 0.75, 0.75)
negro = (0, 0, 0)
rojo = (0.75, 0, 0)
verde = (0, 0.75, 0)


def dibuja_laberinto(M, fila_entrada, col_entrada, fila_salida, col_salida):
    n_filas = len(M)
    n_cols = len(M[0])
    fig = plt.figure()
    fig.patch.set_facecolor('white')
    ax = plt.gca()

    if fila_entrada is not None and col_entrada is not None:
        ax.add_patch(Rectangle((col_entrada, n_filas - fila_entrada),
                               1, -1, linewidth=0, facecolor=verde,
                               fill=True))
    if fila_salida is not None and col_salida is not None:
        ax.add_patch(Rectangle((col_salida, n_filas - fila_salida),
                               1, -1, linewidth=0, facecolor=rojo,
                               fill=True))

    for fila in range(0, n_filas):
        for col in range(0, n_cols):
            if M[fila][col] == 'W':
                ax.add_patch(Rectangle((col, n_filas - fila), 1, -1,
                                       linewidth=0, facecolor=gris))
            elif M[fila][col] == 'P':
                circ = plt.Circle((col + 0.5, n_filas - fila - 0.5),
                                  radius=0.15, color=negro, fill=True)
                ax.add_patch(circ)

    ax.add_patch(Rectangle((0, 0), n_cols, n_filas, edgecolor=negro,
                           fill=False))
    plt.axis('equal')
    plt.axis('off')
    plt.show()


M = lee_laberinto_de_fichero('maze01_input.txt')  # Algún fichero
# Entra por arriba a la izquierda, sal por abajo a la derecha
if busca_camino_laberinto_wrapper(M, 0, 0, len(M) - 1, len(M[0]) - 1):
    dibuja_laberinto(M, 0, 0, len(M) - 1, len(M[0]) - 1)
