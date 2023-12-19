def nqueens_one_sol(i, free_rows, free_pdiags,
                    free_sdiags, sol):
    n = len(sol)
    sol_found = False

    if i == n:
        return True
    else:
        k = 0
        while not sol_found and k < n:
            if (free_rows[k] and free_pdiags[i - k + n - 1]
                    and free_sdiags[i + k]):

                sol[i] = k

                free_rows[k] = False
                free_pdiags[i - k + n - 1] = False
                free_sdiags[i + k] = False

                sol_found = nqueens_one_sol(i + 1, free_rows,
                                            free_pdiags,
                                            free_sdiags, sol)

                free_rows[k] = True
                free_pdiags[i - k + n - 1] = True
                free_sdiags[i + k] = True

            k = k + 1

        return sol_found


def nqueens_one_sol_wrapper(n):
    free_rows = [True] * n
    free_pdiags = [True] * (2 * n - 1)
    free_sdiags = [True] * (2 * n - 1)
    sol = [None] * n

    if nqueens_one_sol(0, free_rows, free_pdiags,
                       free_sdiags, sol):
        print_chessboard(sol)


def print_chessboard(sol):
    for i in range(0, len(sol)):
        print(sol[i], ' ', end='')
    print()


# Test
nqueens_one_sol_wrapper(8)
