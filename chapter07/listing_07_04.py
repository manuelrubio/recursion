def inorder_traversal(T):
    if T != []:
        inorder_traversal(T[2])  # process left subtree
        print(T[0], ': ', T[1], sep='')  # print key and item
        inorder_traversal(T[3])  # process right subtree


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

inorder_traversal(T)
