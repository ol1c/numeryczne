import numpy as np
import time


def LUD(A):
    return np.tril(A, k=-1),  np.triu(A, k=1), np.diag(np.diag(A))


def JacobiMethod(A, b):
    L, U, D = LUD(A)
    x = np.ones(len(b))

    D_inv_diag = 1.0 / np.diag(D)
    M = -(L + U) * D_inv_diag[:, np.newaxis]
    w = b / np.diag(D)

    rNorm = [np.linalg.norm(A @ x - b)]
    iterations = 0
    start = time.perf_counter_ns()
    while rNorm[-1] > 1e-9 and iterations < 1000:
        x = M @ x + w
        rNorm.append(np.linalg.norm(A @ x - b))
        iterations += 1
    end = time.perf_counter_ns()
    return iterations, rNorm, end - start


def GaussSeidlMethod(A, b):
    L, U, D = LUD(A)
    x = np.ones(len(b))

    T = D + L
    T_inv = np.linalg.inv(T)
    M = -T_inv @ U
    w = T_inv @ b

    rNorm = [np.linalg.norm(A @ x - b)]
    iterations = 0
    start = time.perf_counter_ns()
    while rNorm[-1] > 1e-9 and iterations < 1000:
        x = M @ x + w
        rNorm.append(np.linalg.norm(A @ x - b))
        iterations += 1
    end = time.perf_counter_ns()
    return iterations, rNorm, end - start


def lu(A):
    N = A.shape[0]
    L = np.zeros([N, N])
    U = A.copy().astype(float)
    P = np.eye(N)
    for i in range(N):
        maxRow = np.argmax(abs(U[i:, i])) + i
        if i != maxRow:
            U[[i, maxRow]] = U[[maxRow, i]]
            P[[i, maxRow]] = P[[maxRow, i]]
            L[[i,maxRow], :i] = L[[maxRow, i], :i]
        L[i][i] = 1
        for j in range(i+1, N):
            L[j][i] = U[j][i] / U[i][i]
            U[j] -= L[j][i] * U[i]
    return L, U, P


def LUMethod(A, b):
    start = time.perf_counter_ns()
    L, U, P = lu(A)
    factorizationTime = time.perf_counter_ns() - start

    start = time.perf_counter_ns()
    y = np.linalg.inv(L) @ (P @ b)
    x = np.linalg.inv(U) @ y
    directTime = time.perf_counter_ns() - start
    return np.linalg.norm(A @ x - b), factorizationTime + directTime
