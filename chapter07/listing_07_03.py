def towers_of_Hanoi(n, o, d, a):
    if n == 1:
        print('Move disk', n, 'from rod', o, 'to rod', d)
    else:
        towers_of_Hanoi(n - 1, o, a, d)
        print('Move disk', n, 'from rod', o, 'to rod', d)
        towers_of_Hanoi(n - 1, a, d, o)


def towers_of_Hanoi_alt(n, o, d, a):
    if n > 0:
        towers_of_Hanoi_alt(n - 1, o, a, d)
        print('Move disk', n, 'from rod', o, 'to rod', d)
        towers_of_Hanoi_alt(n - 1, a, d, o)


towers_of_Hanoi(4, 'O', 'D', 'A')


# Test
print()
towers_of_Hanoi_alt(4, 'O', 'D', 'A')
print()

print()
towers_of_Hanoi(1, 'O', 'D', 'A')
print()
towers_of_Hanoi_alt(1, 'O', 'D', 'A')
print()

print()
towers_of_Hanoi(2, 'O', 'D', 'A')
print()
towers_of_Hanoi_alt(2, 'O', 'D', 'A')
print()

print()
towers_of_Hanoi(3, 'O', 'D', 'A')
print()
towers_of_Hanoi_alt(3, 'O', 'D', 'A')
