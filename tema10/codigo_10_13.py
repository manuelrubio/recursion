__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def element_pico(a, inf, sup):
    if inf == sup:
        return inf
    else:
        mitad = (inf + sup) // 2

        if a[mitad] > a[mitad + 1]:
            return element_pico(a, 0, mitad)
        else:
            return element_pico(a, mitad, sup)
