def generate_permutations_alt(i, available, sol, elements):
    # Base case
    if i == len(elements):
        print_permutation(sol)  # complete solution
    else:
        # Generate candidate elements
        for k in range(0, len(elements)):

            # Check candidate validity
            if available[k]:

                # Include candidate in partial solution
                sol[i] = elements[k]

                # k-th candidate no longer available
                available[k] = False

                # Expand partial solution at position i+1
                generate_permutations_alt(i + 1, available,
                                          sol, elements)

                # k-th candidate available again
                available[k] = True


def generate_permutations_alt_wrapper(elements):
    available = [True] * (len(elements))
    sol = [None] * (len(elements))
    generate_permutations_alt(0, available, sol, elements)


# Test
def print_permutation(sol):
    for i in range(0, len(sol)):
        print(sol[i], ' ', end='')
    print()


# Test
generate_permutations_alt_wrapper(['a', 'b', 'c'])
print()

generate_permutations_alt_wrapper(['a', 3, False])
