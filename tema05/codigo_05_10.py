__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def inserta_arbol_binario(x, T):
    if T == []:
        T.extend([x[0], x[1], [], []])
    else:
        if x[0] < T[0]:
            if T[2] == []:
                T[2] = [x[0], x[1], [], []]
            else:
                inserta_arbol_binario(x, T[2])
        else:
            if T[3] == []:
                T[3] = [x[0], x[1], [], []]
            else:
                inserta_arbol_binario(x, T[3])


# Prueba
a = [('John', '2006/05/08'),
     ('Luke', '1976/07/31'),
     ('Lara', '1987/08/23'),
     ('Sara', '1995/03/14'),
     ('Paul', '2000/01/13'),
     ('Anna', '1999/12/03'),
     ('Emma', '2002/08/23')]

T = []
for i in range(0, len(a)):
    inserta_arbol_binario(a[i], T)
    print(T)
    print()
