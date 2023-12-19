def generate_permutations(i, sol, elements):
    # Base case
    if i == len(elements):
        print_permutation(sol)  # complete solution
    else:
        # Generate candidate elements
        for k in range(0, len(elements)):

            # Check candidate validity
            if not elements[k] in sol[0:i]:

                # Include candidate in partial solution
                sol[i] = elements[k]

                # Expand partial solution at position i+1
                generate_permutations(i + 1, sol, elements)

                # Remove candidate from partial solution
                sol[i] = None  # not necessary


def generate_permutations_wrapper(elements):
    sol = [None] * (len(elements))
    generate_permutations(0, sol, elements)


def print_permutation(sol):
    for i in range(0, len(sol)):
        print(sol[i], ' ', end='')
    print()


# Test
generate_permutations_wrapper(['a', 'b', 'c'])
print()

generate_permutations_wrapper(['a', 3, False])
