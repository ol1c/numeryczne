function [dates, y, rmse_values, M, c, ya] = calculate_rmse()
% 1) Wyznacza pierwiastek błędu średniokwadratowego w zależności od stopnia
%    aproksymacji wielomianowej danych przedstawiających produkcję energii.
% 2) Wyznacza i przedstawia na wykresie aproksymację wielomianową wysokiego
%    stopnia danych przedstawiających produkcję energii.
% Dla kraju C oraz źródła energii S:
% dates - wektor energy_2025.C.S.Dates (daty pomiaru produkcji energii)
% y - wektor energy_2025.C.S.EnergyProduction (poziomy miesięcznych produkcji energii)
% rmse_values(i,1) - RMSE wyznaczony dla wektora y i wielomianu i-tego stopnia
%     Rozmiar kolumnowego wektora wynosi length(y)-1.
% M - stopień wielomianu aproksymacyjnego przedstawionego na wykresie
% c - współczynniki wielomianu aproksymacyjnego przedstawionego na wykresie:
%       c = [c_M; ...; c_1; c_0]
% ya - wartości wielomianu aproksymacyjnego wyznaczone dla punktów danych
%       (rozmiar wektora ya powinien być taki sam jak rozmiar wektora y)

    M = 90; % stopień wielomianu aproksymacyjnego (dla wykresu)

    load energy_2025

    dates = energy_2025.Poland.Coal.Dates; % TODO
    y = energy_2025.Poland.Coal.EnergyProduction; % TODO

    N = numel(y);
    degrees = 1:N-1;

    x = linspace(0,1,N)';

    rmse_values = zeros(numel(degrees),1);

    % Oblicz RMSE dla każdego stopnia
    for m = degrees
        % TODO:
        c = polyfit_qr(x, y, m);
        c = c(end:-1:1); % odwrócenie kolejności wektora c: dostosowanie do polyval
        ya = polyval(c, x);
        result = 0;
        for i = 1:numel(x)
            result = result + (ya(i) - y(i))^2;
        end

        rmse_values(m) = sqrt(result/numel(x));
    end

    % Aproksymacja wielomianu wysokiego stopnia (dla wykresu)
    c = polyfit_qr(x, y, M);
    c = c(end:-1:1); % odwrócenie kolejności wektora c: dostosowanie do polyval

    ya = polyval(c, x);

    % TODO:
    % Wykresy
    subplot(2,1,1);
    plot(degrees, rmse_values);
    xlabel('stopnie wielomianu');
    ylabel('wartość RMSE');
    title('Zmiana RMSE w zależności od stopnia wielomianu')
    subplot(2,1,2);
    plot(dates, y, 'k-', 'DisplayName', 'dane orignalne');
    hold on;
    plot(dates, ya, 'b-', 'DisplayName', 'aproksymacja');
    xlabel("data");
    ylabel("poziom produkcji energii [TWh]");
    title("Produkcja energii z węgal w Polsce");
    legend('Location', 'best');
    hold off;


end

function c = polyfit_qr(x, y, M)
    % Wyznacza współczynniki wielomianu aproksymacyjnego stopnia M
    % z zastosowaniem rozkładu QR.
    % c - kolumnowy wektor wsp. wielomianu c = [c_0; ...; c_M]

    A = zeros(numel(x),M+1); % macierz Vandermonde o rozmiarze [n,M+1]
    for i = 1:numel(x)
        for j = 1:M+1
            A(i,j) = x(i)^(j-1);
        end
    end
    % TODO:
    [q1, r1] = qr(A, 0); % economy QR factorization
    c = r1 \ (q1.' * y);
end