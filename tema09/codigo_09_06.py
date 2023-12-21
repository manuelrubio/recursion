__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def reloj(n, o, d, a):
    if n > 0:
        hanoi_antireloj(n - 1, o, a, d)
        print('Mueve disco', n, 'desde torre', o, 'hasta torre', d)
        hanoi_antireloj(n - 1, a, d, o)


def hanoi_antireloj(n, o, d, a):
    if n > 0:
        hanoi_antireloj(n - 1, o, d, a)
        print('Mueve disco', n, 'desde torre', o, 'hasta torre', a)
        reloj(n - 1, d, o, a)
        print('Mueve disco', n, 'desde torre', a, 'hasta torre', d)
        hanoi_antireloj(n - 1, o, d, a)


# Test
reloj(1, 'O', 'D', 'A')
print()
reloj(2, 'O', 'D', 'A')
print()
reloj(3, 'O', 'D', 'A')
print()
reloj(4, 'O', 'D', 'A')
print()

print()
hanoi_antireloj(1, 'O', 'D', 'A')
print()
hanoi_antireloj(2, 'O', 'D', 'A')
print()
hanoi_antireloj(3, 'O', 'D', 'A')
print()
hanoi_antireloj(4, 'O', 'D', 'A')
print()
