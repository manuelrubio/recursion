__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def genera_permutaciones(i, sol, elementos):
    # Caso base
    if i == len(elementos):
        imprime_permutacion(sol)  # Solución completa
    else:
        # Genera candidatos
        for k in range(0, len(elementos)):

            # Comprueba validez del candidato
            if not elementos[k] in sol[0:i]:

                # Incluye candidato en solución parcial
                sol[i] = elementos[k]

                # Expande la solución parcial a partir de la posición i+1
                genera_permutaciones(i + 1, sol, elementos)

                # Elimina candidato de solución parcial
                sol[i] = None  # Opcional (no necesario)

def genera_permutaciones_wrapper(elementos):
    sol = [None] * (len(elementos))
    genera_permutaciones(0, sol, elementos)


def imprime_permutacion(sol):
    for i in range(0, len(sol)):
        print(sol[i], ' ', end='')
    print()


# Test
genera_permutaciones_wrapper(['a', 'b', 'c'])
print()

genera_permutaciones_wrapper(['a', 3, False])
