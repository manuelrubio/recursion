# lists a and b are sorted in ascending order
def merge(a, b):
    if a == []:
        return b
    elif b == []:
        return a
    else:
        if a[0] < b[0]:
            return [a[0]] + merge(a[1:], b)
        else:
            return [b[0]] + merge(a, b[1:])


# Test
print(merge([], []))
print(merge([1, 3, 5], []))
print(merge([], [2, 4, 6]))
print(merge([1], [2, 4, 6]))
print(merge([3], [2, 4, 6]))
print(merge([7], [2, 4, 6]))
print(merge([1, 5], [2, 4, 6]))
print(merge([3, 9], [2, 4, 6]))
print(merge([7, 9], [2, 4, 6]))
print(merge([1, 3, 5, 7], [2, 4, 6]))
