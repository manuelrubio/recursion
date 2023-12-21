__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def genera_subconjuntos(i, sol, elementos):
    # Caso base
    if i == len(elementos):
        # Imprime el subconjunto (solución completa)
        imprime_subconjunto_binario(sol, elementos)
    else:
        # Genera candidatos
        for k in range(0, 2):
            
            # Incluye candidato en solución parcial
            sol[i] = k
            
            # Expande la solución parcial a partir de la posición i+1
            genera_subconjuntos(i + 1, sol, elementos)
            
            # Elimina candidato de solución parcial
            sol[i] = None  # Opcional (no necesario)


def genera_subconjuntos_wrapper(elementos):
    sol = [None] * (len(elementos))
    genera_subconjuntos(0, sol, elementos)


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
genera_subconjuntos_wrapper(['a', 'b', 'c'])
print()

genera_subconjuntos_wrapper(['a', 3, False])
