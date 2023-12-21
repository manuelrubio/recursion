__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def sumatorio_interno(n, m):
    if n <= 0:
        return 0
    else:
        return sumatorio_interno(n - 1, m) + (m + n)


def sumatorio_externa(m, n):
    if m <= 0:
        return 0
    else:
        return sumatorio_externa(m - 1, n) + sumatorio_interno(n, m)


# Test
for m in range(0, 5):
    for n in range(0, 5):
        print(sumatorio_externa(m, n), ' = ', m * n *
              (m + n + 2) // 2)  # comprobación
