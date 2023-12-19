def tokenize_unary(s):
    if not s or s == ' ' or s == '\t':
        return []
    elif len(s) == 1:
        return [s]
    elif s[0] == ' ' or s[0] == '\t':
        return tokenize_unary(s[1:])
    elif s[0].isdigit() or s[0] == '-':
        if s[0].isdigit() and (s[1] == ' ' or s[1] == '\t'):
            return [s[0]] + tokenize(s[2:])
        else:
            t = tokenize(s[1:])
            if t == []:
                return [s[0]]
            else:
                if is_number(t[0]):
                    t[0] = s[0] + t[0]
                    return t
                else:
                    return [s[0]] + t
    else:
        if s[0] == '(':
            t = tokenize_unary(s[1:])
        else:
            t = tokenize(s[1:])
        return [s[0]] + t


def tokenize(s):
    if not s or s == ' ' or s == '\t':
        return []
    elif len(s) == 1:
        return [s]
    elif s[0] == ' ' or s[0] == '\t':
        return tokenize(s[1:])
    elif s[0].isdigit():
        if s[1] == ' ' or s[1] == '\t':
            return [s[0]] + tokenize(s[2:])
        else:
            t = tokenize(s[1:])
            if t == []:
                return [s[0]]
            else:
                if is_number(t[0]):
                    t[0] = s[0] + t[0]
                    return t
                else:
                    return [s[0]] + t
    else:
        if s[0] == '(':
            t = tokenize_unary(s[1:])
        else:
            t = tokenize(s[1:])
        return [s[0]] + t


# Test
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


print(tokenize_unary('-(-6 / 3) - (-(4)) + (18-2)'))

print()
s = '-(- (-(- 4* (4 -8 /3))-(4 / 2- 5/ (4*3+2))) ) + 3* 3/(-3* 5+2) -(3 + (4*2)) + (-(4)*7/(5))'
print(tokenize_unary(s))
