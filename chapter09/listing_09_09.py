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
