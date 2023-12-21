__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def contiene_mayor_elemento(a):
    if a == []:
        return False
    else:
        return (2 * a[0] > sum(a)
                or contiene_mayor_elemento(a[1:]))
