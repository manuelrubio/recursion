__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

# Caluculator functions
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


def expresion(tokens):
    if tokens == []:
        raise SyntaxError('Error de sintaxis')
    else:
        contador_parentesis = 0
        i = len(tokens) - 1
        while i > 0 and ((tokens[i] != '+' and tokens[i] != '-')
                         or contador_parentesis > 0):
            if tokens[i] == ')':
                contador_parentesis = contador_parentesis + 1
            if tokens[i] == '(':
                contador_parentesis = contador_parentesis - 1

            i = i - 1

        if i == 0:
            if tokens[0] == '-':
                return - termino_invertido(tokens[1:])
            else:
                return termino(tokens)
        else:
            e = expresion(tokens[0:i])
            t = termino(tokens[i + 1:])
            if tokens[i] == '+':
                return e + t
            else:
                return e - t


def termino(tokens):
    if tokens == []:
        raise SyntaxError('Error de sintaxis')
    else:
        contador_parentesis = 0
        i = len(tokens) - 1
        while i > 0 and ((tokens[i] != '*' and tokens[i] != '/')
                         or contador_parentesis > 0):
            if tokens[i] == ')':
                contador_parentesis = contador_parentesis + 1
            if tokens[i] == '(':
                contador_parentesis = contador_parentesis - 1

            i = i - 1

        if i == 0:
            return factor(tokens)
        else:
            t = termino(tokens[0:i])
            f = factor(tokens[i + 1:])
            if tokens[i] == '*':
                return t * f
            else:
                return t / f


def termino_invertido(tokens):
    if tokens == [] or tokens[0] != '(':
        raise SyntaxError('Error de sintaxis')
    else:
        contador_parentesis = 1
        n = len(tokens)
        i = 1
        while i < n and contador_parentesis > 0:
            if tokens[i] == '(':
                contador_parentesis = contador_parentesis + 1
            if tokens[i] == ')':
                contador_parentesis = contador_parentesis - 1

            i = i + 1

        if i == n:
            return expresion_con_parentesis(tokens)
        else:
            p = expresion_con_parentesis(tokens[0:i])
            t = termino(tokens[i + 1:])
            if tokens[i] == '*':
                return p * t
            else:
                return p / t


def factor(tokens):
    if tokens == []:
        raise SyntaxError('Error de sintaxis')
    elif len(tokens) == 1:
        if es_numero(tokens[0]):
            return float(tokens[0])
        else:
            raise SyntaxError('Error de sintaxis')
    else:
        return expresion_con_parentesis(tokens)


def expresion_con_parentesis(tokens):
    if tokens == [] or tokens[0] != '(' or tokens[-1] != ')':
        raise SyntaxError('Error de sintaxis')
    else:
        return expresion(tokens[1:-1])


s = '-(- (-(- 4 * (4 - 8 / 3)) - (4 / 2 - 5 / (4 * 3 + 2)))) + \
    3 * 3 / (-3 * 5 + 2) - (3 + (4 * 2)) + (-(4) * 7 / (5))'
print(tokeniza_unitario(s))
print(expresion(tokeniza_unitario(s)))


# Listing 9.14
s = input('> ')
print(expresion(tokeniza_unitario(s)))