__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def lineas_pascal(n):
    if n == 0:
        return [1]
    else:
        fila = [1]
        fila_previa = lineas_pascal(n - 1)
        for i in range(len(fila_previa) - 1):
            fila.append(fila_previa[i] + fila_previa[i + 1])
        fila.append(1)
    return fila


# Prueba
for n in range(0, 6):
    print(lineas_pascal(n))
