def binary_search(a, x, lower, upper):
    if lower > upper:  # empty list
        return -1
    else:
        middle = (lower + upper) // 2

        if x == a[middle]:
            return middle
        elif x < a[middle]:
            return binary_search(a, x, lower, middle - 1)
        else:
            return binary_search(a, x, middle + 1, upper)


def binary_search_wrapper(a, x):
    return binary_search(a, x, 0, len(a) - 1)


# Test
a = []
print(binary_search_wrapper(a, 3))
print()

a = [2]
print(binary_search_wrapper(a, 2))
print(binary_search_wrapper(a, 8))
print()

a = [2, 4]
print(binary_search_wrapper(a, 1))
print(binary_search_wrapper(a, 2))
print(binary_search_wrapper(a, 3))
print(binary_search_wrapper(a, 4))
print(binary_search_wrapper(a, 5))
print()

a = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search_wrapper(a, 3))
print(binary_search_wrapper(a, 0))
print(binary_search_wrapper(a, 1))
print(binary_search_wrapper(a, 2))
print(binary_search_wrapper(a, 8))
print(binary_search_wrapper(a, 13))
print(binary_search_wrapper(a, 17))
print(binary_search_wrapper(a, 19))
print(binary_search_wrapper(a, 32))
print(binary_search_wrapper(a, 42))
print(binary_search_wrapper(a, 20))
