def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


# Test
print(is_number(2541))
print(is_number('one'))
