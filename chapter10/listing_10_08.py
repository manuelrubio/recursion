def add_digits(n):
    if n == 0:
        return 0
    else:
        return add_digits(n // 10) + (n % 10)


def count_digits(n):
    if n == 0:
        return 0
    else:
        return count_digits(n // 10) + 1
