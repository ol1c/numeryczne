function [circles, a, b, r_max] = generate_circles(n_max)
    % n_max określa liczbę wylosowanych okręgów, które zawarte są w prostokącie i nie przecinają oraz nie zawierają innych okręgów.
    % a - długość prostokąta wzdłuż osi x wybrana z zakresu [150, 250]
    % b - długość prostokąta wzdłuż osi y wybrana z zakresu [50, 100]
    % Prostokąt ma wierzchołki w punktach (0,0), (a,0), (a,b) i (0,b).
    % Określa maksymalny promień okręgu (r_max) z zakresu [20, 50]
    a = randi([150, 250]);
    b = randi([50, 100]);
    r_max = randi([20, 50]);

    circles = zeros(n_max, 3);
    for i = 1:n_max
        valid = false;
        while ~valid
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
    end    
end
 