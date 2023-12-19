def sum_first_naturals_5(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 2 * sum_first_naturals_5(n / 2) + (n / 2)**2
    else:
        return (2 * sum_first_naturals_5((n - 1) / 2)
                + ((n + 1) / 2)**2)


# Test
for n in range(1, 11):
    print(sum_first_naturals_5(n), n * (n + 1) // 2)
