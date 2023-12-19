def parenthesized_expression(tokens):
    if tokens == [] or tokens[0] != '(' or tokens[-1] != ')':
        raise SyntaxError('Syntax error')
    else:
        return expression(tokens[1:-1])
