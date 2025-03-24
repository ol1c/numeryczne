function [residuum_norm_direct, residuum_norm_Jacobi, residuum_norm_Gauss_Seidel] = zadanie7_solve()

load filtr_dielektryczny.mat;
[x_direct, residuum_norm_direct] = solve_direct(A, b);
[x_Jacobi, residuum_norm_Jacobi] = solve_Jacobi(A, b);
[x_Gauss_Seidel, residuum_norm_Gauss_Seidel] = solve_Gauss_Seidel(A, b);
end