def occurrences_in_list(a, x):
    if a == []:
        return 0
    else:
        return int(a[0] == x) + occurrences_in_list(a[1:], x)


# Test
a = [4, 3, 5, 4, 1, 5, 5, 5, 2, 6, 6, 1, 1, 3, 4, 3, 4]
print(occurrences_in_list(a, 0))
print(occurrences_in_list(a, 1))
print(occurrences_in_list(a, 2))
print(occurrences_in_list(a, 3))
print(occurrences_in_list(a, 4))
print(occurrences_in_list(a, 5))
print(occurrences_in_list(a, 6))
