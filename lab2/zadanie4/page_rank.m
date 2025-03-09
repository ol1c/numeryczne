function [Edges, I, B, A, b, r] = page_rank()
Edges = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 7;
         4, 6, 3, 4, 5, 5, 6, 7, 5, 6, 4, 6, 4, 7, 6];
I = speye(7);
B = sparse(Edges(2,:), Edges(1,:), 1, 7, 7);
A = spdiags(sum(B, 1)' .^ (-1), 0, 7, 7);
b = (1 - 0.85) / 7 * ones(7, 1);
M = I - 0.85 * B * A;
r = M \ b;

bar(r);
hold on;
title("PageRank");
xlabel("Strony");
ylabel("Współczynnik PR dla stron");
hold off;
end