__copyright__ = "Copyright (C) 2023 Manuel Rubio S�nchez"
__license__ = "MIT License"

def recorrido_en_orden(T):
    if T != []:
        recorrido_en_orden(T[2])  # procesa el sub�rbol izquierdo
        print(T[0], ': ', T[1], sep='')  # imprime la clave y el item
        recorrido_en_orden(T[3])  # procesa el sub�rbol derecho


# Test
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

recorrido_en_orden(T)
