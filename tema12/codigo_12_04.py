__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def genera_permutaciones_alt(i, libres, sol, elementos):
    # Caso base
    if i == len(elementos):
        imprime_permutacion(sol)  # Solución completa
    else:
        # Genera candidatos
        for k in range(0, len(elementos)):

            # Comprueba validez del candidato
            if libres[k]:

                # Incluye candidato en solución parcial
                sol[i] = elementos[k]

                # El k-ésimo candidato ya no está libre
                libres[k] = False

                # Expande la solución parcial a partir de la posición i+1
                genera_permutaciones_alt(i + 1, libres, sol, elementos)

                # El k-ésimo candidato vuelve a estar libre
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
