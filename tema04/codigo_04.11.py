__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def invierte_cadena(s):
    if s == '':
        return ''
    else:
        return invierte_cadena(s[1:]) + s[0]


# Prueba
print(invierte_cadena(''))
print(invierte_cadena('a'))
print(invierte_cadena('ab'))
print(invierte_cadena('abcde'))
