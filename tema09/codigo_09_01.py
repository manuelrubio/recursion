__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def es_par(n):
    if n == 0:
        return True
    else:
        return es_impar(n - 1)


def es_impar(n):
    if n == 0:
        return False
    else:
        return es_par(n - 1)


# Test
for n in range(0, 6):
    print(es_par(n))

print()
for n in range(0, 6):
    print(es_impar(n))
