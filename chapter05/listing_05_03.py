def equal_strings(s, t):
    if len(s) != len(t):
        return False
    elif s == '':
        return True
    else:
        return s[0] == t[0] and equal_strings(s[1:], t[1:])


# Test
print(equal_strings('', ''))
print(equal_strings('a', 'a'))
print(equal_strings('a', 'b'))
print(equal_strings('ab', 'ab'))
print(equal_strings('ab', 'aa'))
print(equal_strings('ab', 'ba'))
print(equal_strings('abc', 'abc'))
