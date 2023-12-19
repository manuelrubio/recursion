def print_knapsack_solution(sol, w, v, C, opt_value):
    n = len(sol)
    k = 0
    while k < n and sol[k] == 0:
        k = k + 1

    total_weight = 0
    if k < n:
        print('(', w[k], ',', v[k], ')', sep='', end='')
        total_weight = total_weight + w[k]

        for i in range(k + 1, n):
            if sol[i] == 1:
                total_weight = total_weight + w[i]
                print(' + ', sep='', end='')
                print('(', w[i], ',', v[i], ')', sep='', end='')

    print(' => ', '(', total_weight, ',', opt_value, ')', sep='')


w = [3, 6, 9, 5]  # List of object weights
v = [7, 2, 10, 4]  # List of object values
C = 15  # Weight capacity of the knapsack
knapsack_0_1_wrapper(w, v, C)
