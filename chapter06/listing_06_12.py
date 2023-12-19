def trominoes(x, y, n, p, q):
    if n == 2:
        if y == q:  # hole in bottom tiles
            if x == p:  # hole in bottom-left tile
                draw_L1(x, y)
            else:  # hole in bottom-right tile
                draw_L2(x, y)
        else:  # hole in top tiles
            if x == p:  # hole in top-left tile
                draw_L3(x, y)
            else:  # hole in top-right tile
                draw_L4(x, y)

    else:
        mid_x = x + n // 2
        mid_y = y + n // 2

        if q < mid_y:  # hole in bottom squares

            if p < mid_x:  # hole in bottom-left square
                draw_L1(mid_x - 1, mid_y - 1)
                trominoes(x, y, n // 2, p, q)
                trominoes(x, mid_y, n // 2, mid_x - 1, mid_y)
                trominoes(mid_x, y, n // 2, mid_x, mid_y - 1)
                trominoes(mid_x, mid_y, n // 2, mid_x, mid_y)
            else:  # hole in bottom-right square
                draw_L2(mid_x - 1, mid_y - 1)
                trominoes(x, y, n // 2, mid_x - 1, mid_y - 1)
                trominoes(x, mid_y, n // 2, mid_x - 1, mid_y)
                trominoes(mid_x, y, n // 2, p, q)
                trominoes(mid_x, mid_y, n // 2, mid_x, mid_y)

        else:  # hole in top squares

            if p < mid_x:  # hole in top-left square
                draw_L3(mid_x - 1, mid_y - 1)
                trominoes(x, y, n // 2, mid_x - 1, mid_y - 1)
                trominoes(x, mid_y, n // 2, p, q)
                trominoes(mid_x, y, n // 2, mid_x, mid_y - 1)
                trominoes(mid_x, mid_y, n // 2, mid_x, mid_y)
            else:  # hole top-right square
                draw_L4(mid_x - 1, mid_y - 1)
                trominoes(x, y, n // 2, mid_x - 1, mid_y - 1)
                trominoes(x, mid_y, n // 2, mid_x - 1, mid_y)
                trominoes(mid_x, y, n // 2, mid_x, mid_y - 1)
                trominoes(mid_x, mid_y, n // 2, p, q)
