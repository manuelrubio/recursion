__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def subcadena_capicua_mas_larga_programacion_dinamica(s):
    n = len(s)
    L = [['' for i in range(n)] for j in range(n)]

    for i in range(n):
        L[i][i] = s[i]

    k = 1
    while k < n:
        i = 0
        j = k
        while j < n:
            if (len(L[i + 1][j - 1]) == j - i - 1
                    and s[i] == s[j]):
                L[i][j] = s[i:j + 1]
            elif len(L[i][j - 1]) >= len(L[i + 1][j]):
                L[i][j] = L[i][j - 1]
            else:
                L[i][j] = L[i + 1][j]

            i = i + 1
            j = j + 1

        k = k + 1

    return L[0][n - 1]


# Test
s = 'abbcbabcbbcbaabcbcbababcbcbc'
print(subcadena_capicua_mas_larga_programacion_dinamica(s))

s = 'ACGTGTACCATCCG'
print(subcadena_capicua_mas_larga_programacion_dinamica(s))
