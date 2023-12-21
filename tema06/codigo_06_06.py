__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def ocurrencias_en_lista(a, x):
    if a == []:
        return 0
    else:
        return int(a[0] == x) + ocurrencias_en_lista(a[1:], x)


# Test
a = [4, 3, 5, 4, 1, 5, 5, 5, 2, 6, 6, 1, 1, 3, 4, 3, 4]
print(ocurrencias_en_lista(a, 0))
print(ocurrencias_en_lista(a, 1))
print(ocurrencias_en_lista(a, 2))
print(ocurrencias_en_lista(a, 3))
print(ocurrencias_en_lista(a, 4))
print(ocurrencias_en_lista(a, 5))
print(ocurrencias_en_lista(a, 6))
