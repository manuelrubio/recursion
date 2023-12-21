__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def cadenas_iguales(s, t):
    if len(s) != len(t):
        return False
    elif s == '':
        return True
    else:
        return s[0] == t[0] and cadenas_iguales(s[1:], t[1:])


# Test
print(cadenas_iguales('', ''))
print(cadenas_iguales('a', 'a'))
print(cadenas_iguales('a', 'b'))
print(cadenas_iguales('ab', 'ab'))
print(cadenas_iguales('ab', 'aa'))
print(cadenas_iguales('ab', 'ba'))
print(cadenas_iguales('abc', 'abc'))
