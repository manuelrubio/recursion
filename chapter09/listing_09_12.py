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
