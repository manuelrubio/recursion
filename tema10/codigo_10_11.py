__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def suelo_log(x, b):
    if x == 1:
        return 0
    else:
        return 1 + suelo_log(x / b, b)
