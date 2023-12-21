__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def f(x):
    return x * x - 2


def biseccion(a, b, f, epsilon):
    z = (a + b) / 2

    if f(z) == 0 or b - a <= 2 * epsilon:
        return z
    elif (f(a) > 0 and f(z) < 0) or (f(a) < 0 and f(z) > 0):
        return biseccion(a, z, f, epsilon)
    else:
        return biseccion(z, b, f, epsilon)


# Imprime una aproximación de la raíz cuadrada de 2
print(biseccion(0, 4, f, 10**(-10)))
