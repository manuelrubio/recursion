# Caluculator functions
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


def expression(tokens):
    if tokens == []:
        raise SyntaxError('Syntax error')
    else:
        par_counter = 0
        i = len(tokens) - 1
        while i > 0 and ((tokens[i] != '+' and tokens[i] != '-')
                         or par_counter > 0):
            if tokens[i] == ')':
                par_counter = par_counter + 1
            if tokens[i] == '(':
                par_counter = par_counter - 1

            i = i - 1

        if i == 0:
            if tokens[0] == '-':
                return - inverted_term(tokens[1:])
            else:
                return term(tokens)
        else:
            e = expression(tokens[0:i])
            t = term(tokens[i + 1:])
            if tokens[i] == '+':
                return e + t
            else:
                return e - t


def term(tokens):
    if tokens == []:
        raise SyntaxError('Syntax error')
    else:
        par_counter = 0
        i = len(tokens) - 1
        while i > 0 and ((tokens[i] != '*' and tokens[i] != '/')
                         or par_counter > 0):
            if tokens[i] == ')':
                par_counter = par_counter + 1
            if tokens[i] == '(':
                par_counter = par_counter - 1

            i = i - 1

        if i == 0:
            return factor(tokens)
        else:
            t = term(tokens[0:i])
            f = factor(tokens[i + 1:])
            if tokens[i] == '*':
                return t * f
            else:
                return t / f


def inverted_term(tokens):
    if tokens == [] or tokens[0] != '(':
        raise SyntaxError('Syntax error')
    else:
        par_counter = 1
        n = len(tokens)
        i = 1
        while i < n and par_counter > 0:
            if tokens[i] == '(':
                par_counter = par_counter + 1
            if tokens[i] == ')':
                par_counter = par_counter - 1

            i = i + 1

        if i == n:
            return parenthesized_expression(tokens)
        else:
            p = parenthesized_expression(tokens[0:i])
            t = term(tokens[i + 1:])
            if tokens[i] == '*':
                return p * t
            else:
                return p / t


def factor(tokens):
    if tokens == []:
        raise SyntaxError('Syntax error')
    elif len(tokens) == 1:
        if is_number(tokens[0]):
            return float(tokens[0])
        else:
            raise SyntaxError('Syntax error')
    else:
        return parenthesized_expression(tokens)


def parenthesized_expression(tokens):
    if tokens == [] or tokens[0] != '(' or tokens[-1] != ')':
        raise SyntaxError('Syntax error')
    else:
        return expression(tokens[1:-1])


s = '-(- (-(- 4 * (4 - 8 / 3)) - (4 / 2 - 5 / (4 * 3 + 2)))) + \
    3 * 3 / (-3 * 5 + 2) - (3 + (4 * 2)) + (-(4) * 7 / (5))'
print(tokenize_unary(s))
print(expression(tokenize_unary(s)))


# Listing 9.14
s = input('> ')
print(expression(tokenize_unary(s)))
