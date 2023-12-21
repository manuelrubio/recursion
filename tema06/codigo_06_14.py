__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def calcula_skyline(edificios):
    n = len(edificios)
    if n == 1:
        return ([(edificios[0][0], edificios[0][2]),
                 (edificios[0][1], 0)])
    else:
        skyline1 = calcula_skyline(edificios[0:n // 2])
        skyline2 = calcula_skyline(edificios[n // 2:n])
        return mezcla_skylines(skyline1, skyline2, 0, 0)


# Test
def mezcla_skylines(sky1, sky2, p1, p2):
    if sky1 == []:
        return sky2
    elif sky2 == []:
        return sky1
    else:
        x1 = sky1[0][0]
        x2 = sky2[0][0]
        h1 = sky1[0][1]
        h2 = sky2[0][1]

        if x1 == x2:
            h = max(p1, p2)
            nueva_h = max(h1, h2)
            if h == nueva_h:
                return mezcla_skylines(sky1[1:], sky2[1:], h1, h2)
            else:
                return ([(x1, nueva_h)]
                        + mezcla_skylines(sky1[1:], sky2[1:], h1, h2))

        elif x1 < x2:
            if h1 > p2:
                return ([(x1, h1)]
                        + mezcla_skylines(sky1[1:], sky2, h1, p2))
            elif p1 > p2:
                return ([(x1, p2)]
                        + mezcla_skylines(sky1[1:], sky2, h1, p2))
            else:
                return mezcla_skylines(sky1[1:], sky2, h1, p2)
        else:
            if h2 > p1:
                return ([(x2, h2)]
                        + mezcla_skylines(sky1, sky2[1:], p1, h2))
            elif p2 > p1:
                return ([(x2, p1)]
                        + mezcla_skylines(sky1, sky2[1:], p1, h2))
            else:
                return mezcla_skylines(sky1, sky2[1:], p1, h2)


edificios = [(1, 6, 7), (18, 20, 7), (2, 9, 5), (17, 19, 2),
             (12, 24, 3), (3, 8, 8), (11, 13, 5), (15, 21, 6)]
skyline = calcula_skyline(edificios)
print(skyline)
