# Decomposition: s(a) => s(a[0:n-1]), a[n-1]
def sum_list_limits_1(a, lower, upper):
    if lower > upper:
        return 0
    else:
        return a[upper] + sum_list_limits_1(a, lower, upper - 1)


# Decomposition: s(a) => a[0], s(a[1:n])
def sum_list_limits_2(a, lower, upper):
    if lower > upper:
        return 0
    else:
        return a[lower] + sum_list_limits_2(a, lower + 1, upper)


# Decomposition: s(a) => s(a[0:n//2]), s(a[n//2:n])
def sum_list_limits_3(a, lower, upper):
    if lower > upper:
        return 0
    elif lower == upper:
        return a[lower]  # or a[upper]
    else:
        middle = (upper + lower) // 2
        return (sum_list_limits_3(a, lower, middle)
                + sum_list_limits_3(a, middle + 1, upper))


# Some list:
a = [5, -1, 3, 2, 4, -3]

# Function calls:
print(sum_list_limits_1(a, 0, len(a) - 1))
print(sum_list_limits_2(a, 0, len(a) - 1))
print(sum_list_limits_3(a, 0, len(a) - 1))
