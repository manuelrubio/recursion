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
