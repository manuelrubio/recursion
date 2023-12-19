def is_even_incorrect(n):
    if n == 0:
        return True
    else:
        return is_even_incorrect(n - 2)


# Test
print(is_even_incorrect(4))
print(is_even_incorrect(0))
# maximum recursion depth exceeded in comparison
print(is_even_incorrect(7))
