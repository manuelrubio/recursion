__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def expresion_con_parentesis(tokens):
    if tokens == [] or tokens[0] != '(' or tokens[-1] != ')':
        raise SyntaxError('Error de sintaxis')
    else:
        return expresion(tokens[1:-1])
