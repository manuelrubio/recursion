def bst_search(T, key):
    if T == []:
        return None
    elif T[0] == key:
        return T[1]  # return the root item
    elif key < T[0]:
        return bst_search(T[2], key)  # search in left subtree
    else:
        return bst_search(T[3], key)  # search in right subtree


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

print(bst_search(T, 'Sara'))
print(bst_search(T, 'Emma'))
print(bst_search(T, 'John'))
print(bst_search(T, 'Anna'))
print(bst_search(T, 'Lucy'))
