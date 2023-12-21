__copyright__ = "Copyright (C) 2023 Manuel Rubio Sánchez"
__license__ = "MIT License"

def residuo(n):
    if n < 10:
        return n
    else:
        return residuo(residuo(n // 10) + n % 10)


# Test
print(residuo(79868))
