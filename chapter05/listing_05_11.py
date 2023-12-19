def get_smaller_than_or_equal_to(a, x):
    if a == []:
        return []
    elif a[0] <= x:
        return [a[0]] + get_smaller_than_or_equal_to(a[1:], x)
    else:
        return get_smaller_than_or_equal_to(a[1:], x)


def get_greater_than(a, x):
    if a == []:
        return []
    elif a[0] > x:
        return [a[0]] + get_greater_than(a[1:], x)
    else:
        return get_greater_than(a[1:], x)


# Test
print(get_smaller_than_or_equal_to([1], 0))
print(get_smaller_than_or_equal_to([1], 1))
print(get_smaller_than_or_equal_to([1], 2))
print()

print(get_smaller_than_or_equal_to([1, 5], 0))
print(get_smaller_than_or_equal_to([1, 5], 1))
print(get_smaller_than_or_equal_to([1, 5], 3))
print(get_smaller_than_or_equal_to([1, 5], 5))
print(get_smaller_than_or_equal_to([1, 5], 6))
print()

print(get_greater_than([1], 0))
print(get_greater_than([1], 1))
print(get_greater_than([1], 2))
print()

print(get_greater_than([1, 5], 0))
print(get_greater_than([1, 5], 1))
print(get_greater_than([1, 5], 3))
print(get_greater_than([1, 5], 5))
print(get_greater_than([1, 5], 6))
