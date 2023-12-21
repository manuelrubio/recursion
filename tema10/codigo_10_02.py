__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def metodo_misterio_1(s):
    if s:
        print(s[0], end='')
        metodo_misterio_1(s[1:])


def metodo_misterio_2(s):
    if s:
        metodo_misterio_2(s[1:])
        print(s[0], end='')


s = 'Word'
metodo_misterio_1(s)
print()
metodo_misterio_2(s)
