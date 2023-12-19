def majority_element_in_list(a):
    n = len(a)
    if n == 0:
        return (False, None, 0)
    elif n == 1:
        return (True, a[0], 1)
    else:
        b = a[0:n // 2]
        c = a[n // 2:n]

        t = majority_element_in_list(b)
        if t[0]:
            occurrences = occurrences_in_list(c, t[1])
            if t[2] + occurrences > n / 2:
                return (True, t[1], t[2] + occurrences)

        t = majority_element_in_list(c)
        if t[0]:
            occurrences = occurrences_in_list(b, t[1])
            if t[2] + occurrences > n / 2:
                return (True, t[1], t[2] + occurrences)

        return (False, None, 0)


# Test
def occurrences_in_list(a, x):
    if a == []:
        return 0
    else:
        return int(a[0] == x) + occurrences_in_list(a[1:], x)


a = [4, 4, 5, 4, 1, 2, 4, 3]
print(majority_element_in_list(a))

a = [4, 4, 5, 4, 1, 2, 4, 4]
print(majority_element_in_list(a))

a = [4, 4, 5, 4, 4, 2, 4, 4]
print(majority_element_in_list(a))
