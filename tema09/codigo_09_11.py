__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def termino_invertido(tokens):
    if tokens == [] or tokens[0] != '(':
        raise SyntaxError('Error de sintaxis')
    else:
        contador_parentesis = 1
        n = len(tokens)
        i = 1
        while i < n and contador_parentesis > 0:
            if tokens[i] == '(':
                contador_parentesis = contador_parentesis + 1
            if tokens[i] == ')':
                contador_parentesis = contador_parentesis - 1

            i = i + 1

        if i == n:
            return expresion_con_parentesis(tokens)
        else:
            p = expresion_con_parentesis(tokens[0:i])
            t = termino(tokens[i + 1:])
            if tokens[i] == '*':
                return p * t
            else:
                return p / t
