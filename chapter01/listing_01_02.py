def sum_first_naturals_2(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    elif n % 2:
        return (3 * sum_first_naturals_2((n - 1) / 2)
                + sum_first_naturals_2((n + 1) / 2))
    else:
        return (3 * sum_first_naturals_2(n / 2)
                + sum_first_naturals_2(n / 2 - 1))


# Test
for n in range(1, 11):
    print(sum_first_naturals_2(n), n * (n + 1) // 2)
