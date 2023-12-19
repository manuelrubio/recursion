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
