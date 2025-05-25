function [x, y, z, zmin, lake_volume] = compute_lake_volume_monte_carlo()
    % Wyznacza objętość jeziora metodą Monte Carlo.
    %
    % x/y/z - wektory wierszowe, które zawierają współrzędne x/y/z punktów
    %       wylosowanych w celu wyznaczenia przybliżonej objętości jeziora
    % zmin - minimalna dopuszczalna wartość współrzędnej z losowanych punktów
    % lake_volume - objętość jeziora wyznaczona metodą Monte Carlo

    N = 1e6;
    x = 100*rand(1,N); % [m]
    y = 100*rand(1,N); % [m]
    
    zmin = -45;
    z = zmin*rand(1,N);
    ft_xy = get_lake_depth(x, y);
    N1 = 0;
    for i=1:N
        if(ft_xy(i) <= z(i))
            N1 = N1 + 1;
        end
    end
    lake_volume = 100 * 100 * abs(zmin) * N1 / N;

end