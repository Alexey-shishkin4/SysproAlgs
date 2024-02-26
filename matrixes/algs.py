import numpy as np


def matrix_addition(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]


def matrix_subtraction(matrix1, matrix2):
    return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]


def zeros_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    max_dim = max(n, m)
    new_dim = 1
    while new_dim < max_dim:
        new_dim *= 2
    padded_matrix = [[0] * new_dim for _ in range(new_dim)]
    for i in range(n):
        for j in range(m):
            padded_matrix[i][j] = matrix[i][j]
    return padded_matrix

def matrix_multi(first, second):
    res = [[0 for _ in range(len(second[0]))] for _ in range(len(first))]
    for i in range(len(first)):
        for j in range(len(second[0])):
            for k in range(len(second)):
                res[i][j] += first[i][k] * second[k][j]
    return res


def recur_matrix_multi(first, second):
    length = len(first)
    if length <= 64:
        return matrix_multi(first, second)
    a = [row[:length // 2] for row in first[:length // 2]]
    b = [row[length // 2:] for row in first[:length // 2]]
    c = [row[:length // 2] for row in first[length // 2:]]
    d = [row[length // 2:] for row in first[length // 2:]]

    e = [row[:length // 2] for row in second[:length // 2]]
    f = [row[length // 2:] for row in second[:length // 2]]
    g = [row[:length // 2] for row in second[length // 2:]]
    h = [row[length // 2:] for row in second[length // 2:]]

    ae = recur_matrix_multi(a, e)
    bg = recur_matrix_multi(b, g)
    af = recur_matrix_multi(a, f)
    bh = recur_matrix_multi(b, h)
    ce = recur_matrix_multi(c, e)
    dg = recur_matrix_multi(d, g)
    cf = recur_matrix_multi(c, f)
    dh = recur_matrix_multi(d, h)

    res = [[0 for _ in range(length)] for _ in range(length)]
    res[:length // 2][:length//2] = matrix_addition(ae, bg)
    res[:length // 2][length // 2: length] = matrix_addition(af, bh)
    res[length // 2: length][:length // 2] = matrix_addition(ce, dg)
    res[length // 2: length][length // 2: length] = matrix_addition(cf, dh)
    return res


def shtrassen_matrix(first, second):
    n1, m1 = len(first), len(first[0])
    n2, m2 = len(second), len(second[0])

    if n1 != m1 or n2 != m2 or n1 != n2:
        raise ValueError

    n = max(n1, n2, m1, m2)
    if n & (n - 1) != 0:
        new_size = 1
        while new_size < n:
            new_size *= 2
        first = zeros_matrix(first)
        second = zeros_matrix(second)

    length = len(first)
    if length <= 64:
        return matrix_multi(first, second)
    a = [row[:length // 2] for row in first[:length // 2]]
    b = [row[length // 2:] for row in first[:length // 2]]
    c = [row[:length // 2] for row in first[length // 2:]]
    d = [row[length // 2:] for row in first[length // 2:]]

    e = [row[:length // 2] for row in second[:length // 2]]
    f = [row[length // 2:] for row in second[:length // 2]]
    g = [row[:length // 2] for row in second[length // 2:]]
    h = [row[length // 2:] for row in second[length // 2:]]

    p1 = shtrassen_matrix(a, matrix_subtraction(f, h))
    p2 = shtrassen_matrix(matrix_addition(a, b), h)
    p3 = shtrassen_matrix(matrix_addition(c, d), e)
    p4 = shtrassen_matrix(d, matrix_subtraction(g, e))
    p5 = shtrassen_matrix(matrix_addition(a, d), matrix_addition(e, h))
    p6 = shtrassen_matrix(matrix_subtraction(b, d), matrix_addition(g, h))
    p7 = shtrassen_matrix(matrix_subtraction(a, c), matrix_addition(e, f))

    q1 = matrix_addition(matrix_subtraction(matrix_addition(p5, p4), p2), p6)
    q2 = matrix_addition(p1, p2)
    q3 = matrix_addition(p3, p4)
    q4 = matrix_subtraction(matrix_subtraction(matrix_addition(p1, p5), p3), p7)

    res = [[0 for _ in range(length)] for _ in range(length)]
    res[:length // 2][:length // 2] = q1
    res[:length // 2][length // 2: length] = q2
    res[length // 2: length][:length // 2] = q3
    res[length // 2: length][length // 2: length] = q4

    return res