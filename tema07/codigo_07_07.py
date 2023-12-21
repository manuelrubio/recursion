__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def subcadena_capicua_mas_larga_alt(s):
    n = len(s)
    if n <= 1:
        return s
    else:
        s_aux_1 = subcadena_capicua_mas_larga_alt(s[1:n - 1])
        if len(s_aux_1) == n - 2 and s[0] == s[n - 1]:
            return s
        else:
            s_aux_2 = subcadena_capicua_mas_larga_alt(s[1:n])
            s_aux_3 = subcadena_capicua_mas_larga_alt(
                s[0:n - 1])
            if len(s_aux_2) > len(s_aux_3):
                return s_aux_2
            else:
                return s_aux_3


# Test
def es_capicua(s):
    n = len(s)
    if n <= 1:
        return True
    else:
        return (s[0] == s[n - 1]) and es_capicua(s[1:n - 1])


print(subcadena_capicua_mas_larga_alt(''))
print(subcadena_capicua_mas_larga_alt('a'))
print(subcadena_capicua_mas_larga_alt('ab'))
print(subcadena_capicua_mas_larga_alt('aa'))
print(subcadena_capicua_mas_larga_alt('aba'))
print(subcadena_capicua_mas_larga_alt('abaa'))
print(subcadena_capicua_mas_larga_alt('abaab'))
print(subcadena_capicua_mas_larga_alt('ACGTGTACCATCCG'))
