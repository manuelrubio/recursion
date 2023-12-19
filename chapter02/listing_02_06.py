def is_even_correct(n):
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return is_even_correct(n - 2)


# Test
for n in range(0, 10):
    print(n, ' is even: ', is_even_correct(n), sep='')
