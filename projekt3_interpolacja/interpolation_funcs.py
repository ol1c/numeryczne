import numpy as np


def fine_nodes(N):
    d = 1 / (N - 1)
    return [i * d for i in range(N)]


def chebyshev_nodes(N):
    # nodes = [1-(np.cos((i-1)/(N-1)*np.pi)+1)/2 for i in range(N)]
    # return  nodes
    nodes = 0.5 * (1 - np.cos(np.pi * np.arange(N) / (N - 1)))
    return nodes.tolist()

def get_nodes(x, y, grid):
    start_idx = 0
    nodes_y = []
    for xi in grid:
        for idx in range(start_idx, len(x)):
            if xi == x[idx]:
                start_idx = idx+1
                nodes_y.append(y[idx])
                break
            elif xi < x[idx]:
                start_idx = idx
                nodes_y.append((y[idx-1]+y[idx])/2)
                break
    return grid, nodes_y


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
