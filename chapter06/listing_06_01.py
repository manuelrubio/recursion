def is_list_sorted(a):
    n = len(a)
    if n <= 1:
        return True
    else:
        return (is_list_sorted(a[0:n // 2])
                and a[n // 2 - 1] <= a[n // 2]
                and is_list_sorted(a[n // 2:n]))


# Test
print(is_list_sorted([]))
print(is_list_sorted([4]))
print(is_list_sorted([3, 7]))
print(is_list_sorted([4, 2]))
print(is_list_sorted([1, 4, 7]))
print(is_list_sorted([1, 9, 7]))
