__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def es_capicua(s):
    n = len(s)
    if n <= 1:
        return True
    else:
        return (s[0] == s[n - 1]) and es_capicua(s[1:n - 1])


# Test
print(es_capicua(''))
print(es_capicua('a'))
print(es_capicua('ab'))
print(es_capicua('aa'))
print(es_capicua('aba'))
print(es_capicua('cba'))
print(es_capicua('abcba'))
print(es_capicua('dbcba'))
print(es_capicua('abcda'))
