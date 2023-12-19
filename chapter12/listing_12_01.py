def generate_subsets(i, sol, elements):
    # Base case
    if i == len(elements):
        # Print complete solution
        print_subset_binary(sol, elements)
    else:
        # Generate candidate elements
        for k in range(0, 2):

            # Include candidate in partial solution
            sol[i] = k

            # Expand partial solution at position i+1
            generate_subsets(i + 1, sol, elements)

            # Remove candidate from partial solution
            sol[i] = None  # optional


def generate_subsets_wrapper(elements):
    sol = [None] * (len(elements))
    generate_subsets(0, sol, elements)


def print_subset_binary(sol, elements):
    no_elements = True
    print('{', end='')
    for i in range(0, len(sol)):
        if sol[i] == 1:
            if no_elements:
                print(elements[i], sep='', end='')
                no_elements = False
            else:
                print(', ', elements[i], sep='', end='')
    print('}')


# Test
generate_subsets_wrapper(['a', 'b', 'c'])
print()

generate_subsets_wrapper(['a', 3, False])
