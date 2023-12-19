def generate_subsets_alt(sol, a):
    # Base case
    if len(sol) == len(a):
        # Print complete solution
        print_subset_binary(sol, a)
    else:
        # Generate candidate elements
        for k in range(0, 2):

            # Include candidate in partial solution
            sol = sol + [k]

            # Expand partial solution at position i+1
            generate_subsets_alt(sol, a)

            # Remove candidate from partial solution
            del sol[-1]


def generate_subsets_alt_wrapper(elements):
    sol = []
    generate_subsets_alt(sol, elements)


# Test
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


generate_subsets_alt_wrapper(['a', 'b', 'c'])
print()

generate_subsets_alt_wrapper(['a', 3, False])
