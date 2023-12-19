def print_subset_sum(i, sol, psum, elements, x):
    # Base case
    if psum == x:
        print_subset_binary(sol, elements)
    elif i < len(elements):
        # Generate candidates
        for k in range(0, 2):

            # Check if recursion tree can be pruned
            if psum + k * elements[i] <= x:

                # Expand partial solution
                sol[i] = k

                # Update sum related to partial solution
                psum = psum + k * elements[i]

                # Try to expand partial solution
                print_subset_sum(i + 1, sol, psum, elements, x)

                # not necessary:
                #psum = psum - k*elements[i]

        # Make sure a 0 indicates the absence of an element
        sol[i] = 0


def print_subset_sum_wrapper(elements, x):
    sol = [0] * (len(elements))
    print_subset_sum(0, sol, 0, elements, x)


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


print_subset_sum_wrapper([2, 6, 3, 5], 8)
print()
print_subset_sum_wrapper([1, 2, 3, 5, 6, 7, 9], 13)
