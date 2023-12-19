def equal_strings_tail(s, t):
    if len(s) != len(t):
        return False
    elif s == '':
        return True
    elif s[0] != t[0]:
        return False
    else:
        return equal_strings_tail(s[1:], t[1:])


# Test
print(equal_strings_tail('', ''))
print(equal_strings_tail('a', 'a'))
print(equal_strings_tail('a', 'b'))
print(equal_strings_tail('ab', 'ab'))
print(equal_strings_tail('ab', 'aa'))
print(equal_strings_tail('ab', 'ba'))
print(equal_strings_tail('abc', 'abc'))
