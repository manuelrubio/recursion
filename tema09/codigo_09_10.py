__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

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
