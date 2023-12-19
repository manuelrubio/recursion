def sum_first_naturals_4(n):
    if n == 1:
        return 1
    else:
        return 2 * sum_first_naturals_4(n // 2) + (n // 2)**2
