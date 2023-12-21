__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

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
