__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def merge_sort(a):
    n = len(a)
    if n <= 1:
        return a
    else:
        a1 = merge_sort(a[0:n // 2])
        a2 = merge_sort(a[n // 2:n])
        return mezcla(a1, a2)


# Test
def mezcla(a, b):
    if a == []:
        return b
    elif b == []:
        return a
    else:
        if a[0] < b[0]:
            return [a[0]] + mezcla(a[1:], b)
        else:
            return [b[0]] + mezcla(a, b[1:])


print(merge_sort([]))
print(merge_sort([5]))
print(merge_sort([3, 5]))
print(merge_sort([5, 3]))
print(merge_sort([1, 3, 5]))
print(merge_sort([1, 5, 3]))
print(merge_sort([3, 1, 5]))
print(merge_sort([3, 5, 1]))
print(merge_sort([5, 1, 3]))
print(merge_sort([5, 3, 1]))
print(merge_sort(
    [72, 28, 30, 80, 18, 94, 54, 95, 12, 6, 26, 43, 18]))
