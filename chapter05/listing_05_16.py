def compute_wood(t, h):
    if t == []:
        return 0
    else:
        if t[0] > h:
            return t[0] - h + compute_wood(t[1:], h)
        else:
            return compute_wood(t[1:], h)


# Test
t = [5, 4, 3, 12, 8, 7, 5, 10, 7, 8,
     4, 4, 11, 8, 7, 1, 9, 4, 3, 5]
print(compute_wood(t, 12))
print(compute_wood(t, 11))
print(compute_wood(t, 10))
print(compute_wood(t, 9))
print(compute_wood(t, 8))
print(compute_wood(t, 7))
