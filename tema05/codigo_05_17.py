__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def recolecta_madera(t, madera, inf, sup):
    mitad_h = (inf + sup) // 2
    madera_en_la_mitad = calcula_madera(t, mitad_h)

    if madera_en_la_mitad == madera or inf == sup:
        return mitad_h
    elif inf == sup - 1:
        if calcula_madera(t, sup) >= madera:
            return sup
        else:
            return inf
    elif madera_en_la_mitad > madera:
        return recolecta_madera(t, madera, mitad_h, sup)
    else:
        return recolecta_madera(t, madera, inf, mitad_h - 1)


# Test
def calcula_madera(t, h):
    if t == []:
        return 0
    else:
        if t[0] > h:
            return t[0] - h + calcula_madera(t[1:], h)
        else:
            return calcula_madera(t[1:], h)


t = [5, 4, 3, 12, 8, 7, 5, 10, 7, 8,
     4, 4, 11, 8, 7, 1, 9, 4, 3, 5]
for madera in range(1, 12):
    print(recolecta_madera(t, madera, 0, max(t)))
