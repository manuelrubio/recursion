def contains_greatest_element(a):
    if a == []:
        return False
    else:
        return (2 * a[0] > sum(a)
                or contains_greatest_element(a[1:]))
