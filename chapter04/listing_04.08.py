def inner_sum(n, m):
    if n <= 0:
        return 0
    else:
        return inner_sum(n - 1, m) + (m + n)


def outer_sum(m, n):
    if m <= 0:
        return 0
    else:
        return outer_sum(m - 1, n) + inner_sum(n, m)


# Test
for m in range(0, 5):
    for n in range(0, 5):
        print(outer_sum(m, n), ' = ', m * n *
              (m + n + 2) // 2)  # check correctness
