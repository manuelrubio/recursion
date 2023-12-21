__copyright__ = "Copyright (C) 2023 Manuel Rubio S�nchez"
__license__ = "MIT License"

def genera_permutaciones_alt(i, libres, sol, elementos):
    # Caso base
    if i == len(elementos):
        imprime_permutacion(sol)  # Soluci�n completa
    else:
        # Genera candidatos
        for k in range(0, len(elementos)):

            # Comprueba validez del candidato
            if libres[k]:

                # Incluye candidato en soluci�n parcial
                sol[i] = elementos[k]

                # El k-�simo candidato ya no est� libre
                libres[k] = False

                # Expande la soluci�n parcial a partir de la posici�n i+1
                genera_permutaciones_alt(i + 1, libres, sol, elementos)

                # El k-�simo candidato vuelve a estar libre
                libres[k] = True


def genera_permutaciones_alt_wrapper(elementos):
    libres = [True] * (len(elementos))
    sol = [None] * (len(elementos))
    genera_permutaciones_alt(0, libres, sol, elementos)


# Test
def imprime_permutacion(sol):
    for i in range(0, len(sol)):
        print(sol[i], ' ', end='')
    print()


# Test
genera_permutaciones_alt_wrapper(['a', 'b', 'c'])
print()

genera_permutaciones_alt_wrapper(['a', 3, False])
