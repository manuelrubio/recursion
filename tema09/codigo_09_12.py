__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

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
