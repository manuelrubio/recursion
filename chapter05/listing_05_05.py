def linear_search_tail(a, x):
    n = len(a)
    if a == []:
        return -1
    elif a[n - 1] == x:
        return n - 1
    else:
        return linear_search_tail(a[:n - 1], x)


# Test
a = []
print(linear_search_tail(a, 3))
print()

a = [2]
print(linear_search_tail(a, 2))
print(linear_search_tail(a, 8))
print()

a = [2, 4]
print(linear_search_tail(a, 1))
print(linear_search_tail(a, 2))
print(linear_search_tail(a, 3))
print(linear_search_tail(a, 4))
print(linear_search_tail(a, 5))
print()

a = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(linear_search_tail(a, 3))
print(linear_search_tail(a, 0))
print(linear_search_tail(a, 1))
print(linear_search_tail(a, 2))
print(linear_search_tail(a, 8))
print(linear_search_tail(a, 13))
print(linear_search_tail(a, 17))
print(linear_search_tail(a, 19))
print(linear_search_tail(a, 32))
print(linear_search_tail(a, 42))
print(linear_search_tail(a, 20))
