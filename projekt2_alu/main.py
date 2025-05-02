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

def plotTime(x, time1, time2, time3):
    plt.figure(figsize=(12, 7))
    plt.subplots_adjust(bottom=0.15, top=0.95)
    plt.subplot(2, 1, 1)
    plt.plot(x, time1, label="metoda Jacobiego")
    plt.plot(x, time2, label="metoda Gaussa-Seidla")
    plt.plot(x, time3, label="metoda rozkładu LU")
    plt.legend()
    plt.xlabel("rozmiar macieży N")
    plt.ylabel("czas potrzebny do obliczenia [ns]")
    plt.title("Porównanie czasu potzrebnego do rozwiązania równania")
    plt.subplot(2, 1, 2)
    plt.semilogy(x, time1, label="metoda Jacobiego")
    plt.semilogy(x, time2, label="metoda Gaussa-Seidla")
    plt.semilogy(x, time3, label="metoda rozkładu LU")
    plt.legend()
    plt.xlabel("rozmiar macieży N")
    plt.ylabel("czas potrzebny do obliczenia [ns]")
    plt.title("Porównanie czasu potzrebnego do rozwiązania równania (skala log)")
    plt.tight_layout()
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
    return x, np.linalg.norm(A @ x - b), factorizationTime + directTime

# # zad A
# N = 1208
# A = np.zeros([N, N])
# np.fill_diagonal(A, 13)
# np.fill_diagonal(A[1:], -1)
# np.fill_diagonal(A[:,1:], -1)
# np.fill_diagonal(A[2:], -1)
# np.fill_diagonal(A[:,2:], -1)
# b = np.sin([n * 8 for n in range(N)])
#
# # zad B
# x, iterations, rNorm, calculationTime = JacobiMethod(A, b)
# print("\nMetoda Jacobiego")
# print("Iteracje potrzebne do rozwiązania:", iterations)
# print("Czas potrzebny do rozwiązania:", calculationTime, "ns")
# plotSemilogy([i for i in range(iterations+1)], rNorm, "Zmiana normy residuum dla metody Jacobiego")
#
# x, iterations, rNorm, calculationTime = GaussSeidlMethod(A, b)
# print("\nMetoda Gaussa-Seidla")
# print("Iteracje potrzebne do rozwiązania:", iterations)
# print("Czas potrzebny do rozwiązania:", calculationTime, "ns")
# plotSemilogy([i for i in range(iterations+1)], rNorm, "Zmiana normy residuum dla metody Gaussa-Seidla")
#
# # zad C
# np.fill_diagonal(A, 3)
# x, iterations, rNorm, calculationTime = JacobiMethod(A, b)
# print("\nMetoda Jacobiego")
# print("Iteracje potrzebne do rozwiązania:", iterations)
# print("Czas potrzebny do rozwiązania:", calculationTime, "ns")
# plotSemilogy([i for i in range(iterations+1)], rNorm, "Zmiana normy residuum dla metody Jacobiego")
#
# x, iterations, rNorm, calculationTime = GaussSeidlMethod(A, b)
# print("\nMetoda Gaussa-Seidla")
# print("Iteracje potrzebne do rozwiązania:", iterations)
# print("Czas potrzebny do rozwiązania:", calculationTime, "ns")
# plotSemilogy([i for i in range(iterations+1)], rNorm, "Zmiana normy residuum dla metody Gaussa-Seidla")
#
# # zad D
# x, rNorm, calculationTime = LUMethod(A, b)
# print("\nMetoda rozkładu LU")
# print("Czas potrzebny do rozwiązania:", calculationTime, "ns")
# print("Residuum norm:", rNorm)

# zad E
size = [100, 500, 1000, 2000, 3000, 4000, 5000]
JacobiTime = []
GaussSeidlTime = []
LUTime = []
for N in size:
    print(N)
    A = np.zeros([N, N])
    np.fill_diagonal(A, 13)
    np.fill_diagonal(A[1:], -1)
    np.fill_diagonal(A[:, 1:], -1)
    np.fill_diagonal(A[2:], -1)
    np.fill_diagonal(A[:, 2:], -1)
    b = np.sin([n * 8 for n in range(N)])
    x, iterations, rNorm, calculationTime = JacobiMethod(A, b)
    JacobiTime.append(calculationTime*1e-9)
    x, iterations, rNorm, calculationTime = GaussSeidlMethod(A, b)
    GaussSeidlTime.append(calculationTime*1e-9)
    x, rNorm, calculationTime = LUMethod(A, b)
    LUTime.append(calculationTime*1e-9)
plotTime(size, JacobiTime, GaussSeidlTime, LUTime)

