def sum_first_naturals(n):
    if n == 1:
        return 1  # Base case
    else:
        return sum_first_naturals(n - 1) + n  # Recursive case


# Test
for n in range(1, 11):
    print(sum_first_naturals(n), n * (n + 1) // 2)
