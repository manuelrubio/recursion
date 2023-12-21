__copyright__ = "Copyright (C) 2023 Manuel Rubio S�nchez"
__license__ = "MIT License"

def n_reinas_todas_sols(i, filas_libres, diagP_libres,
                    diagS_libres, sol):
    n = len(sol)

    # Comprueba si la soluci�n parcial est� completa
    if i == n:
        imprime_solucion(sol)  # procesa la soluci�n
    else:

        # Genera todos los candidatos que pudieran ser 
        # introducidos en la soluci�n parcial
        for k in range(0, n):

            # Comprueba si la soluci�n parcial con el 
            # k-�simo candidato ser�a v�lida
            if (filas_libres[k] and diagP_libres[i - k + n - 1]
                    and diagS_libres[i + k]):

                # Introduce el candidato k en la soluci�n parcial
                sol[i] = k

                # Actualiza estructuras de datos, habiendo incluido
                # el candidato k en la soluci�n parcial
                filas_libres[k] = False
                diagP_libres[i - k + n - 1] = False
                diagS_libres[i + k] = False

                # Llamada recursiva para seguir insertando m�s candidatos
                # en la soluci�n parcial
                n_reinas_todas_sols(i + 1, filas_libres, diagP_libres,
                                diagS_libres, sol)

                # Reestablece los valores de las estructuras de datos al estado
                # en el que el candidato k no aparece en la soluci�n parcial
                filas_libres[k] = True
                diagP_libres[i - k + n - 1] = True
                diagS_libres[i + k] = True


def n_reinas_wrapper(n):
    filas_libres = [True] * n
    diagP_libres = [True] * (2 * n - 1)
    diagS_libres = [True] * (2 * n - 1)
    sol = [None] * n
    n_reinas_todas_sols(0, filas_libres, diagP_libres, diagS_libres, sol)


# Test
def imprime_solucion(sol):
    for i in range(0, len(sol)):
        print(sol[i], ' ', end='')
    print()


n_reinas_wrapper(4)
print()
n_reinas_wrapper(8)
