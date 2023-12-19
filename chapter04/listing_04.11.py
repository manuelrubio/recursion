def reverse_string(s):
    if s == '':
        return ''
    else:
        return reverse_string(s[1:]) + s[0]


# Test
print(reverse_string(''))
print(reverse_string('a'))
print(reverse_string('ab'))
print(reverse_string('abcde'))
