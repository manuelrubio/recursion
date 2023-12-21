__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def tokeniza_unitario(s):
    if not s or s == ' ' or s == '\t':
        return []
    elif len(s) == 1:
        return [s]
    elif s[0] == ' ' or s[0] == '\t':
        return tokeniza_unitario(s[1:])
    elif s[0].isdigit() or s[0] == '-':
        if s[0].isdigit() and (s[1] == ' ' or s[1] == '\t'):
            return [s[0]] + tokeniza(s[2:])
        else:
            t = tokeniza(s[1:])
            if t == []:
                return [s[0]]
            else:
                if es_numero(t[0]):
                    t[0] = s[0] + t[0]
                    return t
                else:
                    return [s[0]] + t
    else:
        if s[0] == '(':
            t = tokeniza_unitario(s[1:])
        else:
            t = tokeniza(s[1:])
        return [s[0]] + t


def tokeniza(s):
    if not s or s == ' ' or s == '\t':
        return []
    elif len(s) == 1:
        return [s]
    elif s[0] == ' ' or s[0] == '\t':
        return tokeniza(s[1:])
    elif s[0].isdigit():
        if s[1] == ' ' or s[1] == '\t':
            return [s[0]] + tokeniza(s[2:])
        else:
            t = tokeniza(s[1:])
            if t == []:
                return [s[0]]
            else:
                if es_numero(t[0]):
                    t[0] = s[0] + t[0]
                    return t
                else:
                    return [s[0]] + t
    else:
        if s[0] == '(':
            t = tokeniza_unitario(s[1:])
        else:
            t = tokeniza(s[1:])
        return [s[0]] + t


# Test
def es_numero(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


print(tokeniza_unitario('-(-6 / 3) - (-(4)) + (18-2)'))

print()
s = '-(- (-(- 4* (4 -8 /3))-(4 / 2- 5/ (4*3+2))) ) + 3* 3/(-3* 5+2) -(3 + (4*2)) + (-(4)*7/(5))'
print(tokeniza_unitario(s))
