def merge_skylines(sky1, sky2, p1, p2):
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
            new_h = max(h1, h2)
            if h == new_h:
                return merge_skylines(sky1[1:], sky2[1:],
                                      h1, h2)
            else:
                return ([(x1, new_h)]
                        + merge_skylines(sky1[1:], sky2[1:],
                                         h1, h2))

        elif x1 < x2:
            if h1 > p2:
                return ([(x1, h1)]
                        + merge_skylines(sky1[1:], sky2,
                                         h1, p2))
            elif p1 > p2:
                return ([(x1, p2)]
                        + merge_skylines(sky1[1:], sky2,
                                         h1, p2))
            else:
                return merge_skylines(sky1[1:], sky2,
                                      h1, p2)

        else:
            if h2 > p1:
                return ([(x2, h2)]
                        + merge_skylines(sky1, sky2[1:],
                                         p1, h2))
            elif p2 > p1:
                return ([(x2, p1)]
                        + merge_skylines(sky1, sky2[1:],
                                         p1, h2))
            else:
                return merge_skylines(sky1, sky2[1:], p1, h2)


# Test
skyline1 = [(1, 7), (3, 8), (8, 5), (9, 0)]
skyline2 = [(2, 4), (3, 6), (7, 2), (11, 0)]
print(merge_skylines(skyline1, skyline2, 0, 0))
