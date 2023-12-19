def peak_element(a, lower, upper):
    if lower == upper:
        return lower
    else:
        half = (lower + upper) // 2

        if a[half] > a[half + 1]:
            return peak_element(a, 0, half)
        else:
            return peak_element(a, half, upper)
