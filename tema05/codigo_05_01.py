__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def contiene_digito(n, d):
    if n < 10:
        return n == d
    else:
        return (n % 10 == d) or contiene_digito(n // 10, d)


# Test
print(contiene_digito(0, 3))
print(contiene_digito(2, 3))
print(contiene_digito(3, 3))
print(contiene_digito(12, 3))
print(contiene_digito(13, 3))
print(contiene_digito(35, 3))
print(contiene_digito(33, 3))
print(contiene_digito(19862, 3))
print(contiene_digito(19863, 3))
print(contiene_digito(19832, 3))
print(contiene_digito(39812, 3))
print(contiene_digito(33333, 3))
