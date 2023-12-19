def linear_search_linear(a, x, n):
    if a == []:
        return -n - 1
    elif a[0] == x:
        return 0
    else:
        return 1 + linear_search_linear(a[1:], x, n)


def linear_search_linear_wrapper(a, x):
    return linear_search_linear(a, x, len(a))


# Test
a = []
print(linear_search_linear_wrapper(a, 3))
print()

a = [2]
print(linear_search_linear_wrapper(a, 2))
print(linear_search_linear_wrapper(a, 8))
print()

a = [2, 4]
print(linear_search_linear_wrapper(a, 1))
print(linear_search_linear_wrapper(a, 2))
print(linear_search_linear_wrapper(a, 3))
print(linear_search_linear_wrapper(a, 4))
print(linear_search_linear_wrapper(a, 5))
print()

a = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(linear_search_linear_wrapper(a, 3))
print(linear_search_linear_wrapper(a, 0))
print(linear_search_linear_wrapper(a, 1))
print(linear_search_linear_wrapper(a, 2))
print(linear_search_linear_wrapper(a, 8))
print(linear_search_linear_wrapper(a, 13))
print(linear_search_linear_wrapper(a, 17))
print(linear_search_linear_wrapper(a, 19))
print(linear_search_linear_wrapper(a, 32))
print(linear_search_linear_wrapper(a, 42))
print(linear_search_linear_wrapper(a, 20))
