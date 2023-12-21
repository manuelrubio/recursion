__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def subcadena_capicua_mas_larga(s):
    n = len(s)
    if es_capicua(s):
        return s
    else:
        s_aux_1 = subcadena_capicua_mas_larga(s[1:n])
        s_aux_2 = subcadena_capicua_mas_larga(s[0:n - 1])
        if len(s_aux_1) > len(s_aux_2):
            return s_aux_1
        else:
            return s_aux_2


# Test
def es_capicua(s):
    n = len(s)
    if n <= 1:
        return True
    else:
        return (s[0] == s[n - 1]) and es_capicua(s[1:n - 1])


print(subcadena_capicua_mas_larga(''))
print(subcadena_capicua_mas_larga('a'))
print(subcadena_capicua_mas_larga('ab'))
print(subcadena_capicua_mas_larga('aa'))
print(subcadena_capicua_mas_larga('aba'))
print(subcadena_capicua_mas_larga('abaa'))
print(subcadena_capicua_mas_larga('abaab'))
print(subcadena_capicua_mas_larga('ACGTGTACCATCCG'))
