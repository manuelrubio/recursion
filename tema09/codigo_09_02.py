__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def juega_Alicia(n):
    if n <= 2:
        print('Alicia gana')
    elif n & 1:
        # Alicia quita una piedra
        juega_Bob(n - 1)  # El turno pasa a Bob
    else:
        # Alice quita dos piedras
        juega_Bob(n - 2)  # El turno pasa a Bob


def juega_Bob(n):
    if n == 1:
        print('Bob gana')
    else:
        # Bob quita una piedra
        juega_Alicia(n - 1)  # El turno pasa a Alicia


# Test
for n in range(1, 11):
    juega_Bob(n)

print()
for n in range(1, 11):
    juega_Alicia(n)
