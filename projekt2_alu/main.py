import math
import matplotlib.pyplot as plt
import numpy as np
import time


def plotSemilogy(x, y, title):
    plt.figure(figsize=(12, 7))
    plt.subplots_adjust(bottom=0.15, top=0.95)
    plt.semilogy(x, y)
    plt.title(title)
    plt.xlabel("Iteracje")
    plt.ylabel("Norma residuum")
    plt.show()


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
    while rNorm[-1] > 1e-9 and iterations < 700:
        x = M @ x + w
        rNorm.append(np.linalg.norm(A @ x - b))
        iterations += 1
    end = time.perf_counter_ns()
    return x, iterations, rNorm, end - start


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
    while rNorm[-1] > 1e-9 and iterations < 700:
        x = M @ x + w
        rNorm.append(np.linalg.norm(A @ x - b))
        iterations += 1
    end = time.perf_counter_ns()
    return x, iterations, rNorm, end - start

# zad A
N = 1208
A = np.zeros([N, N])
for i in range(N):
    A[i][i] = 13
    if i < N-1:
        A[i][i+1] = -1
        A[i+1][i] = -1
        if i < N-2:
            A[i][i+2] = -1
            A[i+2][i] = -1
b = np.sin([n * 8 for n in range(N)])

# zad B
x, iterations, rNorm, calculationTime = JacobiMethod(A, b)
print("\nMetoda Jacobiego")
print("Iteracje potrzebne do rozwiązania:", iterations)
print("Czas potrzebny do rozwiązania:", calculationTime, "ns")
plotSemilogy([i for i in range(iterations+1)], rNorm, "Zmiana normy residuum dla metody Jacobiego")

x, iterations, rNorm, calculationTime = GaussSeidlMethod(A, b)
print("\nMetoda Gaussa-Seidla")
print("Iteracje potrzebne do rozwiązania:", iterations)
print("Czas potrzebny do rozwiązania:", calculationTime, "ns")
plotSemilogy([i for i in range(iterations+1)], rNorm, "Zmiana normy residuum dla metody Gaussa-Seidla")

# zad C
for i in range(N):
    A[i][i] = 3
x, iterations, rNorm, calculationTime = JacobiMethod(A, b)
print("\nMetoda Jacobiego")
print("Iteracje potrzebne do rozwiązania:", iterations)
print("Czas potrzebny do rozwiązania:", calculationTime, "ns")
plotSemilogy([i for i in range(iterations+1)], rNorm, "Zmiana normy residuum dla metody Jacobiego")

x, iterations, rNorm, calculationTime = GaussSeidlMethod(A, b)
print("\nMetoda Gaussa-Seidla")
print("Iteracje potrzebne do rozwiązania:", iterations)
print("Czas potrzebny do rozwiązania:", calculationTime, "ns")
plotSemilogy([i for i in range(iterations+1)], rNorm, "Zmiana normy residuum dla metody Gaussa-Seidla")
