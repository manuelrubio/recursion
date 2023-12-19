def quicksort_variant(a):
    n = len(a)
    if n <= 1:
        return a
    else:
        pivot = a[n // 2]
        v1 = get_smaller_than_or_equal_to(a, pivot)
        v1.remove(pivot)
        v2 = get_greater_than(a, pivot)
        return (quicksort_variant(v1) + [pivot]
                + quicksort_variant(v2))


# Test
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


print(quicksort_variant([]))
print(quicksort_variant([5]))
print(quicksort_variant([3, 5]))
print(quicksort_variant([5, 3]))
print(quicksort_variant([1, 3, 5]))
print(quicksort_variant([1, 5, 3]))
print(quicksort_variant([3, 1, 5]))
print(quicksort_variant([3, 5, 1]))
print(quicksort_variant([5, 1, 3]))
print(quicksort_variant([5, 3, 1]))
print(quicksort_variant(
    [72, 28, 30, 80, 18, 94, 54, 95, 12, 6, 26, 43, 18]))
