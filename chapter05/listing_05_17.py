def collect_wood(t, wood, lower, upper):
    middle_h = (lower + upper) // 2
    wood_at_middle = compute_wood(t, middle_h)

    if wood_at_middle == wood or lower == upper:
        return middle_h
    elif lower == upper - 1:
        if compute_wood(t, upper) >= wood:
            return upper
        else:
            return lower
    elif wood_at_middle > wood:
        return collect_wood(t, wood, middle_h, upper)
    else:
        return collect_wood(t, wood, lower, middle_h - 1)


# Test
def compute_wood(t, h):
    if t == []:
        return 0
    else:
        if t[0] > h:
            return t[0] - h + compute_wood(t[1:], h)
        else:
            return compute_wood(t[1:], h)


t = [5, 4, 3, 12, 8, 7, 5, 10, 7, 8,
     4, 4, 11, 8, 7, 1, 9, 4, 3, 5]
for wood in range(1, 12):
    print(collect_wood(t, wood, 0, max(t)))
