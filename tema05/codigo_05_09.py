__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

# bst = binary search tree
def bst_busqueda(T, key):
    if T == []:
        return None
    elif T[0] == key:
        return T[1]  # devuelve la raíz
    elif key < T[0]:
        return bst_busqueda(T[2], key)  # busca en el subárbol izquierdo
    else:
        return bst_busqueda(T[3], key)  # busca en el subárbol derecho


# Prueba
T = ['Emma',
     '2002/08/23',
     ['Anna', '1999/12/03', [], []],
     ['Paul',
         '2000/01/13',
         ['Lara',
          '1987/08/23',
          ['John', '2006/05/08', [], []],
             ['Luke', '1976/07/31', [], []]],
         ['Sara', '1995/03/14', [], []]]]

print(bst_busqueda(T, 'Sara'))
print(bst_busqueda(T, 'Emma'))
print(bst_busqueda(T, 'John'))
print(bst_busqueda(T, 'Anna'))
print(bst_busqueda(T, 'Lucy'))
