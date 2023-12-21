__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def calcula_madera(t, h):
    if t == []:
        return 0
    else:
        if t[0] > h:
            return t[0] - h + calcula_madera(t[1:], h)
        else:
            return calcula_madera(t[1:], h)


# Test
t = [5, 4, 3, 12, 8, 7, 5, 10, 7, 8,
     4, 4, 11, 8, 7, 1, 9, 4, 3, 5]
print(calcula_madera(t, 12))
print(calcula_madera(t, 11))
print(calcula_madera(t, 10))
print(calcula_madera(t, 9))
print(calcula_madera(t, 8))
print(calcula_madera(t, 7))
