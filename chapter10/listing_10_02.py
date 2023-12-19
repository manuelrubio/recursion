def mystery_method_1(s):
    if s:
        print(s[0], end='')
        mystery_method_1(s[1:])


def mystery_method_2(s):
    if s:
        mystery_method_2(s[1:])
        print(s[0], end='')


s = 'Word'
mystery_method_1(s)
print()
mystery_method_2(s)
