__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def mochila_01(i,C_restante,v_actual,sol,sol_opt,v_opt,p,v,C):
    if i==len(sol):  # Se han analizado todos los objetos
        if v_actual>v_opt:  # Comprueba si se ha encontrado una solución mejor
            # Actualiza el mejor valor y solución
            v_opt = v_actual
            for k in range(0,len(sol)):
                sol_opt[k] = sol[k]
    else:
        for k in range(0,2):  #  Genera candidatos

            # Comprueba si se puede podar el árbol de recursión
            if k*p[i]<=C_restante:

                # Expande la solución parcial
                sol[i]=k

                # Actualiza la capacidad restante y el valor parcial
                nueva_C_restante = C_restante - k*p[i]
                nuevo_v_actual = v_actual + k*v[i]

                # Intenta expandir la solución parcial
                v_opt = mochila_01(i+1,nueva_C_restante, \
                    nuevo_v_actual,sol,sol_opt,v_opt,p,v,C)

    # devuelve el mejor valor encontrado hasta el momento
    return v_opt


def mochila_01_wrapper(w, v, C):
    sol = [0] * (len(w))
    sol_opt = [0] * (len(w))
    total_v = mochila_01(0, C, 0, sol, sol_opt, -1, w, v, C)
    imprime_solucion_mochila(sol_opt, w, v, C, total_v)


# Test
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
mochila_01_wrapper(w, v, C)
