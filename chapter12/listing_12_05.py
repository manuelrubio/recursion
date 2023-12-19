def nqueens_all_sol(i, free_rows, free_pdiags,
                    free_sdiags, sol):
    n = len(sol)

    # Test if the partial solution is a complete solution
    if i == n:
        print_chessboard(sol)  # process the solution
    else:

        # Generate all possible candidates that could
        # be introduced in the partial solution
        for k in range(0, n):

            # Check if the partial solution with the
            # k-th candidate would be valid
            if (free_rows[k] and free_pdiags[i - k + n - 1]
                    and free_sdiags[i + k]):

                # Introduce candidate k in the partial solution
                sol[i] = k

                # Update data structures, indicating that
                # candidate k is in the partial solution
                free_rows[k] = False
                free_pdiags[i - k + n - 1] = False
                free_sdiags[i + k] = False

                # Perform a recursive call in order to include
                # more candidates in the partial solution
                nqueens_all_sol(i + 1, free_rows, free_pdiags,
                                free_sdiags, sol)

                # Eliminate candidate k from the partial
                # solution, and restore the data structures,
                # indicating that candidate k is no longer
                # in the partial solution
                free_rows[k] = True
                free_pdiags[i - k + n - 1] = True
                free_sdiags[i + k] = True


def nqueens_wrapper(n):
    free_rows = [True] * n
    free_pdiags = [True] * (2 * n - 1)
    free_sdiags = [True] * (2 * n - 1)
    sol = [None] * n
    nqueens_all_sol(0, free_rows, free_pdiags, free_sdiags, sol)


# Test
def print_chessboard(sol):
    for i in range(0, len(sol)):
        print(sol[i], ' ', end='')
    print()


nqueens_wrapper(4)
print()
nqueens_wrapper(8)
