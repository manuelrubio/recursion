__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

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


# Prueba
print(get_menor_o_igual([1], 0))
print(get_menor_o_igual([1], 1))
print(get_menor_o_igual([1], 2))
print()

print(get_menor_o_igual([1, 5], 0))
print(get_menor_o_igual([1, 5], 1))
print(get_menor_o_igual([1, 5], 3))
print(get_menor_o_igual([1, 5], 5))
print(get_menor_o_igual([1, 5], 6))
print()

print(get_mayor([1], 0))
print(get_mayor([1], 1))
print(get_mayor([1], 2))
print()

print(get_mayor([1, 5], 0))
print(get_mayor([1, 5], 1))
print(get_mayor([1, 5], 3))
print(get_mayor([1, 5], 5))
print(get_mayor([1, 5], 6))
