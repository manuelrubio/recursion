__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

# scml: subcadena capicúa más larga
def scml_memoizacion(s, L, i, j):
    if len(L[i][j]) > 0:
        return L[i][j]
    elif i > j:
        return ''
    elif i == j:
        L[i][j] = s[i]
        return s[i]
    else:
        if len(L[i + 1][j - 1]) > 0:
            s_aux_1 = L[i + 1][j - 1]
        else:
            s_aux_1 = scml_memoizacion(s, L, i + 1, j - 1)
            L[i + 1][j - 1] = s_aux_1

        if len(s_aux_1) == j - i - 1 and s[i] == s[j]:
            L[i][j] = s[i:j + 1]
            return s[i:j + 1]
        else:
            if len(L[i + 1][j]) > 0:
                s_aux_2 = L[i + 1][j]
            else:
                s_aux_2 = scml_memoizacion(s, L, i + 1, j)
                L[i + 1][j] = s_aux_2

            if len(L[i][j - 1]) > 0:
                s_aux_3 = L[i][j - 1]
            else:
                s_aux_3 = scml_memoizacion(s, L, i, j - 1)
                L[i][j - 1] = s_aux_3

            if len(s_aux_2) > len(s_aux_3):
                return s_aux_2
            else:
                return s_aux_3

# Test
s = 'abbcbabcbbcbaabcbcbababcbcbc'
L = [['' for i in range(len(s))] for j in range(len(s))]
print(scml_memoizacion(s, L, 0, len(s) - 1))

s = 'ACGTGTACCATCCG'
L = [['' for i in range(len(s))] for j in range(len(s))]
print(scml_memoizacion(s, L, 0, len(s) - 1))
