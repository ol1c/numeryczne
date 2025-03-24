function [x,r_norm] = solve_Gauss_Seidel(A, b)
% A - macierz z równania macierzowego A * x = b
% b - wektor prawej strony równania macierzowego A * x = b
% U - macierz trójkątna górna, która zawiera wszystkie elementy macierzy A powyżej głównej diagonalnej,
% T - macierz trójkątna dolna równa A-U
% w - wektor pomocniczy opisany w instrukcji do Laboratorium 3
%       – sprawdź wzór (7) w instrukcji, który definiuje w jako w_{GS}.
% x - rozwiązanie równania macierzowego
% r_norm - wektor norm residuum kolejnych przybliżeń rozwiązania; norm(A*x-b);
% iteration_count - liczba iteracji wymagana do wyznaczenia rozwiązania
%       metodą Gaussa-Seidla

N = length(A);
L = tril(A, -1);
U = triu(A, 1);
D = diag(diag(A));

iteration_count = 0;

T = D + L;
M = -T \ U;
w = T \ b;
x = ones(N,1);

inorm = norm(A*x-b);
r_norm = inorm;
while(inorm>1e-12 && iteration_count<1000)
    %x = M*x + w;
    x = M * x + w;
    inorm = norm(A*x-b);
    iteration_count = iteration_count+1;
    r_norm = inorm;
end
end