function [rand_counts, counts_mean, circles, a, b, r_max] = generate_circles(n_max)
    % n_max określa liczbę wylosowanych okręgów, które zawarte są w prostokącie i nie przecinają oraz nie zawierają innych okręgów.
    % a - długość prostokąta wzdłuż osi x wybrana z zakresu [150, 250]
    % b - długość prostokąta wzdłuż osi y wybrana z zakresu [50, 100]
    % Prostokąt ma wierzchołki w punktach (0,0), (a,0), (a,b) i (0,b).
    % Określa maksymalny promień okręgu (r_max) z zakresu [20, 50
    % rand_counts – wierszowy wektor długości n_max, w którym rand_counts(k) oznacza liczbę losowań przy generowaniu parametrów k-tego okręgu
    % counts_mean – wierszowy wektor długości n_max, gdzie counts_mean(k) to średnia liczba losowań z wszystkich dotychczas zatwierdzonych okręgów (od 1 do k)
    a = randi([150, 250]);
    b = randi([50, 100]);
    r_max = randi([20, 50]);

    circles = zeros(n_max, 3);
    rand_counts = zeros(1, n_max);
    counts_mean = zeros(1, n_max);
    for i = 1:n_max
        valid = false;
        rand_count = 0;
        while ~valid
            rand_count = rand_count + 1;
            R = r_max * rand();
            
                                          %  -|--R--|---a - 2 * R---|--R--|-
            X = R + (a - 2 * R) * rand(); %   R                           |
            Y = R + (b - 2 * R) * rand(); %   -                           |
                                          %   |                           |
            valid = true;                 %   b - 2 * R                   |
            for j = 1:i-1                 %   |                           |
                Xj = circles(j, 1);       %   -                           |
                Yj = circles(j, 2);       %   R                           |
                Rj = circles(j, 3);       %  -|---------------------------|-

                % Sprawdzenie czy okręgi się przecinają lub zawierają
                dist = sqrt((X - Xj)^2 + (Y - Yj)^2);
                if dist < (R + Rj) 
                    valid = false;
                    break;
                end
            end
        end
        % Zapisanie okręgu do macierzy
        circles(i, :) = [X, Y, R];
        rand_counts(i) = rand_count;
    end
    counts_mean = cumsum(rand_counts) ./ (1:n_max);
    
    subplot(2, 1, 1);
    plot(rand_counts, '.', 'MarkerSize', 3);
    xlabel("K okrąg [k]");
    ylabel("Ilość prób");
    title("Liczba losowań dla każdego okręgu");

    subplot(2, 1, 2);
    plot(counts_mean, '-', 'LineWidth', 2);
    xlabel("Pierwsze k okręgów [k]");
    ylabel("Średnia ilość prób");
    title("Średnia liczba losowań w czasie");

    saveas(gcf, 'zadanie3.png');
end
 