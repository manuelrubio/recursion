def clockwise(n, o, d, a):
    if n > 0:
        counterclockwise(n - 1, o, a, d)
        print('Move disk', n, 'from rod', o, 'to rod', d)
        counterclockwise(n - 1, a, d, o)


def counterclockwise(n, o, d, a):
    if n > 0:
        counterclockwise(n - 1, o, d, a)
        print('Move disk', n, 'from rod', o, 'to rod', a)
        clockwise(n - 1, d, o, a)
        print('Move disk', n, 'from rod', a, 'to rod', d)
        counterclockwise(n - 1, o, d, a)


# Test
clockwise(1, 'O', 'D', 'A')
print()
clockwise(2, 'O', 'D', 'A')
print()
clockwise(3, 'O', 'D', 'A')
print()
clockwise(4, 'O', 'D', 'A')
print()

print()
counterclockwise(1, 'O', 'D', 'A')
print()
counterclockwise(2, 'O', 'D', 'A')
print()
counterclockwise(3, 'O', 'D', 'A')
print()
counterclockwise(4, 'O', 'D', 'A')
print()
