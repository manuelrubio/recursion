__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def contiene_digito_por_cola(n, d):
    if n < 10:
        return n == d
    elif n % 10 == d:
        return True
    else:
        return contiene_digito_por_cola(n // 10, d)


# Test
print(contiene_digito_por_cola(0, 3))
print(contiene_digito_por_cola(2, 3))
print(contiene_digito_por_cola(3, 3))
print(contiene_digito_por_cola(12, 3))
print(contiene_digito_por_cola(13, 3))
print(contiene_digito_por_cola(35, 3))
print(contiene_digito_por_cola(33, 3))
print(contiene_digito_por_cola(19862, 3))
print(contiene_digito_por_cola(19863, 3))
print(contiene_digito_por_cola(19832, 3))
print(contiene_digito_por_cola(39812, 3))
print(contiene_digito_por_cola(33333, 3))
