__copyright__ = "Copyright (C) 2023 Manuel Rubio S�nchez"
__license__ = "MIT License"

def genera_subconjuntos_alt(sol, a):
    # Caso base
    if len(sol) == len(a):
        # Imprime el subconjunto (soluci�n completa)
        imprime_subconjunto_binario(sol, a)
    else:
        # Genera candidatos
        for k in range(0, 2):

            # Incluye candidato en soluci�n parcial
            sol = sol + [k]

            # Expande la soluci�n parcial a partir de la posici�n i+1
            genera_subconjuntos_alt(sol, a)

            # Elimina candidato de soluci�n parcial
            del sol[-1]


def genera_subconjuntos_alt_wrapper(elements):
    sol = []
    genera_subconjuntos_alt(sol, elements)


# Test
def imprime_subconjunto_binario(sol, elementos):
    conjunto_es_vacio = True
    print('{', end='')
    for i in range(0, len(sol)):
        if sol[i] == 1:
            if conjunto_es_vacio:
                print(elementos[i], sep='', end='')
                conjunto_es_vacio = False
            else:
                print(', ', elementos[i], sep='', end='')
    print('}')


# Test
genera_subconjuntos_alt_wrapper(['a', 'b', 'c'])
print()

genera_subconjuntos_alt_wrapper(['a', 3, False])
