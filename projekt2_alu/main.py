import matplotlib.pyplot as plt

from math_func import *
from plots import *

# zad A
N = 1208
A = np.zeros([N, N])
np.fill_diagonal(A, 13)
np.fill_diagonal(A[1:], -1)
np.fill_diagonal(A[:, 1:], -1)
np.fill_diagonal(A[2:], -1)
np.fill_diagonal(A[:, 2:], -1)
b = np.sin([n * 8 for n in range(N)])

# zad B
iterations1, rNorm1, calculationTime1 = JacobiMethod(A, b)
print("\nMetoda Jacobiego")
print("Iteracje potrzebne do rozwiązania:", iterations1)
print("Czas potrzebny do rozwiązania:", calculationTime1*1e-9, "s")

iterations2, rNorm2, calculationTime2 = GaussSeidlMethod(A, b)
print("\nMetoda Gaussa-Seidla")
print("Iteracje potrzebne do rozwiązania:", iterations2)
print("Czas potrzebny do rozwiązania:", calculationTime2*1e-9, "s")
plotSemilogy([i for i in range(iterations1+1)], rNorm1, "metoda Jacobiego", [i for i in range(iterations2+1)], rNorm2, "metoda Gaussa-Seidla")

# zad C
np.fill_diagonal(A, 3)
iterations1, rNorm1, calculationTime1 = JacobiMethod(A, b)
print("\nMetoda Jacobiego")
print("Iteracje potrzebne do rozwiązania:", iterations1)
print("Czas potrzebny do rozwiązania:", calculationTime1*1e-9, "s")

iterations2, rNorm2, calculationTime2 = GaussSeidlMethod(A, b)
print("\nMetoda Gaussa-Seidla")
print("Iteracje potrzebne do rozwiązania:", iterations2)
print("Czas potrzebny do rozwiązania:", calculationTime2*1e-9, "s")
plotSemilogy([i for i in range(iterations1+1)], rNorm1, "metoda Jacobiego", [i for i in range(iterations2+1)], rNorm2, "metoda Gaussa-Seidla")

# zad D
rNorm, calculationTime = LUMethod(A, b)
print("\nMetoda rozkładu LU")
print("Czas potrzebny do rozwiązania:", calculationTime*1e-9, "s")
print("Residuum norm:", rNorm)

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
    iterations, rNorm, calculationTime = JacobiMethod(A, b)
    JacobiTime.append(calculationTime*1e-9)
    iterations, rNorm, calculationTime = GaussSeidlMethod(A, b)
    GaussSeidlTime.append(calculationTime*1e-9)
    rNorm, calculationTime = LUMethod(A, b)
    LUTime.append(calculationTime*1e-9)
plotTime(size, JacobiTime, GaussSeidlTime, LUTime)

