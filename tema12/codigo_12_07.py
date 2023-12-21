__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def imprime_suma_subconjunto(i, sol, suma_parcial, elementos, x):
    # Caso base
    if suma_parcial == x:
        imprime_subconjunto_binario(sol, elementos)
    elif i < len(elementos):
        # Genera candidatos
        for k in range(0, 2):

            # Comprueba si se puede podar el árbol de recursión
            if suma_parcial + k * elementos[i] <= x:

                # Incluye candidato en solución parcial
                sol[i] = k

                # Actualiza la suma parcial
                suma_parcial = suma_parcial + k * elementos[i]

                # Intenta expandir la solución parcial
                imprime_suma_subconjunto(i + 1, sol, suma_parcial, elementos, x)

                # no necesario:
                # suma_parcial = suma_parcial - k*elementos[i]

        # Asegúrate de que un 0 indica la ausencia de un elemento
        sol[i] = 0


def imprime_suma_subconjunto_wrapper(elementos, x):
    sol = [0] * (len(elementos))
    imprime_suma_subconjunto(0, sol, 0, elementos, x)


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


imprime_suma_subconjunto_wrapper([2, 6, 3, 5], 8)
print()
imprime_suma_subconjunto_wrapper([1, 2, 3, 5, 6, 7, 9], 13)
