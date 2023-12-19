def select_sort_rec_alt(a):
    if len(a) <= 1:
        return a
    else:
        b = list(a)
        m = min(b)
        b.remove(m)

        return [m] + select_sort_rec_alt(b)


# Test
print(select_sort_rec_alt([]))
print(select_sort_rec_alt([5]))
print(select_sort_rec_alt([3, 5]))
print(select_sort_rec_alt([5, 3]))
print(select_sort_rec_alt([1, 3, 5]))
print(select_sort_rec_alt([1, 5, 3]))
print(select_sort_rec_alt([3, 1, 5]))
print(select_sort_rec_alt([3, 5, 1]))
print(select_sort_rec_alt([5, 1, 3]))
print(select_sort_rec_alt([5, 3, 1]))
print(select_sort_rec_alt(
    [72, 28, 30, 80, 18, 94, 54, 95, 12, 6, 26, 43, 18]))
