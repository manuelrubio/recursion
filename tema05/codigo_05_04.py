__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def cadenas_iguales_por_cola(s, t):
    if len(s) != len(t):
        return False
    elif s == '':
        return True
    elif s[0] != t[0]:
        return False
    else:
        return cadenas_iguales_por_cola(s[1:], t[1:])


# Test
print(cadenas_iguales_por_cola('', ''))
print(cadenas_iguales_por_cola('a', 'a'))
print(cadenas_iguales_por_cola('a', 'b'))
print(cadenas_iguales_por_cola('ab', 'ab'))
print(cadenas_iguales_por_cola('ab', 'aa'))
print(cadenas_iguales_por_cola('ab', 'ba'))
print(cadenas_iguales_por_cola('abc', 'abc'))
