import numpy as np


def transform_data(x):
    start = x[0]
    end = x[len(x) - 1]
    a = end - start
    copy = x
    for i in range(len(copy)):
        copy[i] = (copy[i] - start) / a
    return copy, [start, a]


def lagrange(nodes_x, nodes_y, new_x):
    size = len(nodes_x)
    new_y = []
    for x in new_x:
        y = 0
        for i in range(size):
            phi = 1
            for j in range(size):
                if j != i:
                    phi = phi * (x - nodes_x[j]) / (nodes_x[i] - nodes_x[j])
            y = y + phi * nodes_y[i]
        new_y.append(y)
        print(x)
    return new_y
