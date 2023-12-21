__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def imprime_solucion_mochila(sol, w, v, C, valor_optimo):
    n = len(sol)
    k = 0
    while k < n and sol[k] == 0:
        k = k + 1

    peso_total = 0
    if k < n:
        print('(', w[k], ',', v[k], ')', sep='', end='')
        peso_total = peso_total + w[k]

        for i in range(k + 1, n):
            if sol[i] == 1:
                peso_total = peso_total + w[i]
                print(' + ', sep='', end='')
                print('(', w[i], ',', v[i], ')', sep='', end='')

    print(' => ', '(', peso_total, ',', valor_optimo, ')', sep='')


w = [3, 6, 9, 5]  # Lista de pesos
v = [7, 2, 10, 4]  # Lista de valores
C = 15  # Capacidad de la mochila en peso
mochila_01_bnb_wrapper(w, v, C)
