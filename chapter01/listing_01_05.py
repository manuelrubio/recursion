# Decomposition: s(a) => s(a[0:n-1]), a[n-1]
def sum_list_length_1(a):
    if len(a) == 0:
        return 0
    else:
        return (sum_list_length_1(a[0:len(a) - 1])
                + a[len(a) - 1])


# Decomposition: s(a) => a[0], s(a[1:n])
def sum_list_length_2(a):
    if len(a) == 0:
        return 0
    else:
        return a[0] + sum_list_length_2(a[1:len(a)])


# Decomposition: s(a) => s(a[0:n//2]), s(a[n//2:n])
def sum_list_length_3(a):
    if len(a) == 0:
        return 0
    elif len(a) == 1:
        return a[0]
    else:
        middle = len(a) // 2
        return (sum_list_length_3(a[0:middle])
                + sum_list_length_3(a[middle:len(a)]))


# Some list:
a = [5, -1, 3, 2, 4, -3]

# Function calls:
print(sum_list_length_1(a))
print(sum_list_length_2(a))
print(sum_list_length_3(a))
