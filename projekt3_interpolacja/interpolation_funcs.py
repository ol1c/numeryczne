import numpy as np


def transform_data(x):
    start = x[0]
    end = x[len(x) - 1]
    a = end - start
    copy = x
    for i in range(len(copy)):
        copy[i] = (copy[i] - start) / a
    return copy, [start, a]


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


def sklejany(nodes_x, nodes_y, new_x):
    start_idx = 0
    size = len(nodes_x)
    if size < 3:
        return [0 for _ in range(len(new_x))]
    new_y = []
    new_size = len(new_x)
    for i in range(2, size, 3):
        h1 = nodes_x[i-1] - nodes_x[i-2]
        h2 = nodes_x[i] - nodes_x[i-1]
        A = np.array([[1, 0, 0, 0, 0, 0, 0, 0],
                      [1, h1, h1**2, h1**3, 0, 0, 0, 0],
                      [0, 0, 0, 0, 1, 0, 0, 0],
                      [0, 0, 0, 0, 1, h2, h2**2, h2**3],
                      [0, 1, h1*2, h1**2*3, 0, -1, 0, 0],
                      [0, 0, 2, 6*h1, 0, 0, -2, 0],
                      [0, 0, 2, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 2, 6*h2]])
        b = np.array([nodes_y[i-2], nodes_y[i-1], nodes_y[i-1], nodes_y[i], 0, 0, 0, 0])
        x = np.linalg.solve(A, b)
        for idx in range(start_idx, new_size):
            if new_x[idx] >= nodes_x[i-1]:
                start_idx = idx
                break
            new_y.append(x[0] + x[1]*(new_x[idx]-nodes_x[i-2]) + x[2]*(new_x[idx]-nodes_x[i-2])**2 + x[3]*(new_x[idx]-nodes_x[i-2])**3)

    i = size - 1
    h1 = nodes_x[i - 1] - nodes_x[i - 2]
    h2 = nodes_x[i] - nodes_x[i - 1]
    A = np.array([[1, 0, 0, 0, 0, 0, 0, 0],
                  [1, h1, h1 ** 2, h1 ** 3, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 1, h2, h2 ** 2, h2 ** 3],
                  [0, 1, h1 * 2, h1 ** 2 * 3, 0, -1, 0, 0],
                  [0, 0, 2, 6 * h1, 0, 0, -2, 0],
                  [0, 0, 2, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 2, 6 * h2]])
    b = np.array([nodes_y[i - 2], nodes_y[i - 1], nodes_y[i - 1], nodes_y[i], 0, 0, 0, 0])
    x = np.linalg.solve(A, b)
    for idx in range(start_idx, new_size):
        if new_x[idx] > nodes_x[i - 1]:
            break
        new_y.append(x[4] + x[5] * (new_x[idx] - nodes_x[i - 1]) + x[6] * (new_x[idx] - nodes_x[i - 1]) ** 2 + x[7] * (
                    new_x[idx] - nodes_x[i - 1]) ** 3)
    return new_y
