def floor_log(x, b):
    if x == 1:
        return 0
    else:
        return 1 + floor_log(x / b, b)
