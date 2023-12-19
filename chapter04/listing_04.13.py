def select_sort_rec(a):
    if len(a) <= 1:
        return a
    else:
        b = list(a)
        min_index = b.index(min(b))
        aux = b[min_index]
        b[min_index] = b[0]
        b[0] = aux

        return [aux] + select_sort_rec(b[1:])


# Test
print(select_sort_rec([]))
print(select_sort_rec([5]))
print(select_sort_rec([3, 5]))
print(select_sort_rec([5, 3]))
print(select_sort_rec([1, 3, 5]))
print(select_sort_rec([1, 5, 3]))
print(select_sort_rec([3, 1, 5]))
print(select_sort_rec([3, 5, 1]))
print(select_sort_rec([5, 1, 3]))
print(select_sort_rec([5, 3, 1]))
print(select_sort_rec(
    [72, 28, 30, 80, 18, 94, 54, 95, 12, 6, 26, 43, 18]))
