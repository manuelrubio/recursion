__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def mochila_01_bnb(i,C_restante,v_actual,max_v,sol,sol_opt,v_opt,p,v,C):
    if i==len(sol):  # Se han analizado todos los objetos
        if v_actual>v_opt:  # Comprueba si se ha encontrado una solución mejor
            # Actualiza el mejor valor y solución
            v_opt = v_actual
            for k in range(0,len(sol)):
                sol_opt[k] = sol[k]
    else:
        for k in range(0,2):  #  Genera candidatos

            # Comprueba si se puede podar el árbol de recursión por capacidad
            if k*p[i]<=C_restante:

               # Actualiza el máximo valor alcanzable
                nuevo_max_v = max_v - (1-k)*v[i]

                # Comprueba si se puede podar el árbol de recursión por valor
                if nuevo_max_v>v_opt:

                    sol[i]=k  # Expande la solución parcial

                    # Actualiza la capacidad restante y el valor parcial
                    nueva_C_restante = C_restante - k*p[i]
                    nuevo_v_actual = v_actual + k*v[i]

                    # Intenta expandir la solución parcial
                    v_opt = mochila_01_bnb(i+1,nueva_C_restante, \
                        nuevo_v_actual,nuevo_max_v,sol,sol_opt,v_opt,p,v,C)

    return v_opt  # devuelve el mejor valor encontrado hasta el momento


def mochila_01_bnb_wrapper(w, v, C):
    sol = [0] * (len(w))
    sol_opt = [0] * (len(w))
    total_v = mochila_01_bnb(0, C, 0, sum(v), sol,
                               sol_opt, -1, w, v, C)
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
mochila_01_bnb_wrapper(w, v, C)
