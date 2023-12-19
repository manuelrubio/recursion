def population_rabbits(n):
    if n <= 2:
        return 1
    else:
        return 1 + children_descendants(n - 2)


def children_descendants(n):
    if n == 0:
        return 0
    else:
        return (population_rabbits(n)
                + children_descendants(n - 1))


# Test
for n in range(1, 11):
    print('{0:4}'.format(population_rabbits(n)), sep=' ', end='')
