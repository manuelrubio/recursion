__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def poblacion_conejos(n):
    if n <= 2:
        return 1
    else:
        return 1 + hijos_descendientes(n - 2)


def hijos_descendientes(n):
    if n == 0:
        return 0
    else:
        return (poblacion_conejos(n)
                + hijos_descendientes(n - 1))


# Test
for n in range(1, 11):
    print('{0:4}'.format(poblacion_conejos(n)), sep=' ', end='')
