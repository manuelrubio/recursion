__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def n_reinas_una_solucion(i, filas_libres, diagP_libres,
                    diagS_libres, sol):
    n = len(sol)
    sol_encontrada = False

    if i == n:
        return True
    else:
        k = 0
        while not sol_encontrada and k < n:
            if (filas_libres[k] and diagP_libres[i - k + n - 1]
                    and diagS_libres[i + k]):

                sol[i] = k

                filas_libres[k] = False
                diagP_libres[i - k + n - 1] = False
                diagS_libres[i + k] = False

                sol_encontrada = n_reinas_una_solucion(i + 1, filas_libres,
                                            diagP_libres,
                                            diagS_libres, sol)

                filas_libres[k] = True
                diagP_libres[i - k + n - 1] = True
                diagS_libres[i + k] = True

            k = k + 1

        return sol_encontrada


def n_reinas_una_solucion_wrapper(n):
    filas_libres = [True] * n
    diagP_libres = [True] * (2 * n - 1)
    diagS_libres = [True] * (2 * n - 1)
    sol = [None] * n

    if n_reinas_una_solucion(0, filas_libres, diagP_libres,
                       diagS_libres, sol):
        imprime_solucion(sol)


def imprime_solucion(sol):
    for i in range(0, len(sol)):
        print(sol[i], ' ', end='')
    print()


# Test
n_reinas_una_solucion_wrapper(8)
