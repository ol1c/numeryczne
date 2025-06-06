function [A,b,L,U,P,y,x,r_norm,t_factorization,t_substitution,t_direct] = ...
        solve_direct()
% A, b - macierz i wektor z równania macierzowego A * x = b
% L - macierz trójkątna dolna pochodząca z wywołania [L,U,P] = lu(A);
% U - macierz trójkątna górna
% P - macierz permutacji
% y - wektor pomocniczy y=L\(P*b)
% x - wektor rozwiązania
% r_norm - norma residuum: norm(A*x-b)
% t_factorization - czas faktoryzacji macierzy A (czas działania funkcji lu)
% t_substitution - czas wyznaczenia rozwiązań równań z macierzami trójkątnymi L i U
% t_direct - czas wyznaczenia rozwiąznia równania macierzowego metodą LU

N = 6000;
[A,b] = generate_matrix(N);

tic;
[L, U, P] = lu(A);
t_factorization = toc;
tic;
y = L \ (P * b);
x =  U \ y;
t_substitution = toc;
r_norm = norm(A * x - b);
t_direct = t_factorization + t_substitution;
r = [t_direct, t_factorization, t_substitution];
bar(r);
title('Porównanie czasu obliczeń');
xlabel('Etapy obliczeń');
ylabel('Czas [s]');
xticklabels({'Całkowity czas', 'Faktoryzacja LU', 'Podstawienie'});
end
 