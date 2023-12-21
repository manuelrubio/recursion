__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def genera_subconjuntos_alt(sol, a):
    # Caso base
    if len(sol) == len(a):
        # Imprime el subconjunto (solución completa)
        imprime_subconjunto_binario(sol, a)
    else:
        # Genera candidatos
        for k in range(0, 2):

            # Incluye candidato en solución parcial
            sol = sol + [k]

            # Expande la solución parcial a partir de la posición i+1
            genera_subconjuntos_alt(sol, a)

            # Elimina candidato de solución parcial
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
