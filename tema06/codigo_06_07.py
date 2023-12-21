__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def elemento_mayoritario_en_lista(a):
    n = len(a)
    if n == 0:
        return (False, None, 0)
    elif n == 1:
        return (True, a[0], 1)
    else:
        b = a[0:n // 2]
        c = a[n // 2:n]

        t = elemento_mayoritario_en_lista(b)
        if t[0]:
            ocurrencias = ocurrencias_en_lista(c, t[1])
            if t[2] + ocurrencias > n / 2:
                return (True, t[1], t[2] + ocurrencias)

        t = elemento_mayoritario_en_lista(c)
        if t[0]:
            ocurrencias = ocurrencias_en_lista(b, t[1])
            if t[2] + ocurrencias > n / 2:
                return (True, t[1], t[2] + ocurrencias)

        return (False, None, 0)


# Test
def ocurrencias_en_lista(a, x):
    if a == []:
        return 0
    else:
        return int(a[0] == x) + ocurrencias_en_lista(a[1:], x)


a = [4, 4, 5, 4, 1, 2, 4, 3]
print(elemento_mayoritario_en_lista(a))

a = [4, 4, 5, 4, 1, 2, 4, 4]
print(elemento_mayoritario_en_lista(a))

a = [4, 4, 5, 4, 4, 2, 4, 4]
print(elemento_mayoritario_en_lista(a))
