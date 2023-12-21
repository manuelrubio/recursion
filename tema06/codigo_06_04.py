__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def quicksort_variante(a):
    n = len(a)
    if n <= 1:
        return a
    else:
        pivote = a[n // 2]
        v1 = get_menor_o_igual(a, pivote)
        v1.remove(pivote)
        v2 = get_mayor(a, pivote)
        return (quicksort_variante(v1) + [pivote]
                + quicksort_variante(v2))


# Test
def get_menor_o_igual(a, x):
    if a == []:
        return []
    elif a[0] <= x:
        return [a[0]] + get_menor_o_igual(a[1:], x)
    else:
        return get_menor_o_igual(a[1:], x)


def get_mayor(a, x):
    if a == []:
        return []
    elif a[0] > x:
        return [a[0]] + get_mayor(a[1:], x)
    else:
        return get_mayor(a[1:], x)


print(quicksort_variante([]))
print(quicksort_variante([5]))
print(quicksort_variante([3, 5]))
print(quicksort_variante([5, 3]))
print(quicksort_variante([1, 3, 5]))
print(quicksort_variante([1, 5, 3]))
print(quicksort_variante([3, 1, 5]))
print(quicksort_variante([3, 5, 1]))
print(quicksort_variante([5, 1, 3]))
print(quicksort_variante([5, 3, 1]))
print(quicksort_variante(
    [72, 28, 30, 80, 18, 94, 54, 95, 12, 6, 26, 43, 18]))
