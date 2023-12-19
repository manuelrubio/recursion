import math


def dot_product(u, v):
    s = 0
    for i in range(0, len(u)):
        s = s + u[i] * v[i]
    return s


def norm_Euclidean(v):
    return math.sqrt(dot_product(v, v))


def cosine(u, v):
    return dot_product(u, v) / norm_Euclidean(u) / norm_Euclidean(v)


# Example
a = [2, 1, 1]
b = [1, 0, 1]
print(cosine(a, b))
