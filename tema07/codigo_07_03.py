__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def torres_de_Hanoi(n, o, d, a):
    if n == 1:
        print('Mueve disco', n, 'desde torre', o, 'hasta torre', d)
    else:
        torres_de_Hanoi(n - 1, o, a, d)
        print('Mueve disco', n, 'desde torre', o, 'hasta torre', d)
        torres_de_Hanoi(n - 1, a, d, o)


def torres_de_Hanoi_alt(n, o, d, a):
    if n > 0:
        torres_de_Hanoi_alt(n - 1, o, a, d)
        print('Mueve disco', n, 'desde torre', o, 'hasta torre', d)
        torres_de_Hanoi_alt(n - 1, a, d, o)


torres_de_Hanoi(4, 'O', 'D', 'A')


# Test
print()
torres_de_Hanoi_alt(4, 'O', 'D', 'A')
print()

print()
torres_de_Hanoi(1, 'O', 'D', 'A')
print()
torres_de_Hanoi_alt(1, 'O', 'D', 'A')
print()

print()
torres_de_Hanoi(2, 'O', 'D', 'A')
print()
torres_de_Hanoi_alt(2, 'O', 'D', 'A')
print()

print()
torres_de_Hanoi(3, 'O', 'D', 'A')
print()
torres_de_Hanoi_alt(3, 'O', 'D', 'A')
