__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def es_numero(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


# Test
print(es_numero(2541))
print(es_numero('one'))
