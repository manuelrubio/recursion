def max_list_length_DaC(a):
    if len(a) == 1:
        return a[0]
    else:
        middle = len(a) // 2
        m1 = max_list_length_DaC(a[0:middle])
        m2 = max_list_length_DaC(a[middle:len(a)])
        return max(m1, m2)


def max_list_limits_DaC(a, lower, upper):
    if lower == upper:
        return a[lower]  # or a[upper]
    else:
        middle = (upper + lower) // 2
        m1 = max_list_limits_DaC(a, lower, middle)
        m2 = max_list_limits_DaC(a, middle + 1, upper)
        return max(m1, m2)


# Some list:
v = [5, -1, 3, 2, 4, 7, 2]

# Function calls:
print(max_list_length_DaC(v))
print(max_list_limits_DaC(v, 0, len(v) - 1))
