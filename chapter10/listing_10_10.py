# Preconditions: n>=m, n>=2, m>=2
def smallest_prime_factor(n, m):
    if n % m == 0:
        return m
    else:
        return smallest_prime_factor(n, m + 1)
