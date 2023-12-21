__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

# lists a and b are sorted in ascending order
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


# Test
print(mezcla([], []))
print(mezcla([1, 3, 5], []))
print(mezcla([], [2, 4, 6]))
print(mezcla([1], [2, 4, 6]))
print(mezcla([3], [2, 4, 6]))
print(mezcla([7], [2, 4, 6]))
print(mezcla([1, 5], [2, 4, 6]))
print(mezcla([3, 9], [2, 4, 6]))
print(mezcla([7, 9], [2, 4, 6]))
print(mezcla([1, 3, 5, 7], [2, 4, 6]))
