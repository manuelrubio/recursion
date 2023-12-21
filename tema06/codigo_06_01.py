__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def lista_esta_ordenada(a):
    n = len(a)
    if n <= 1:
        return True
    else:
        return (lista_esta_ordenada(a[0:n // 2])
                and a[n // 2 - 1] <= a[n // 2]
                and lista_esta_ordenada(a[n // 2:n]))


# Test
print(lista_esta_ordenada([]))
print(lista_esta_ordenada([4]))
print(lista_esta_ordenada([3, 7]))
print(lista_esta_ordenada([4, 2]))
print(lista_esta_ordenada([1, 4, 7]))
print(lista_esta_ordenada([1, 9, 7]))
