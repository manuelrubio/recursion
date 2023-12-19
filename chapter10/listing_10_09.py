def count_consecutive_pairs(a):
    if len(a) == 2:
        return int(a[0] == a[1])
    else:
        return int(a[0] == a[1]) + count_consecutive_pairs(a[1:])
