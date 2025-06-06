function [node_counts, exact_runge, exact_sine, V, interpolated_runge, interpolated_sine] =...
    plot_runge_sine_interpolations()
% Generuje dwa wykresy przedstawiające interpolacje funkcji Rungego oraz
% funkcji sinusoidalnej. Funkcja zwraca
% 1) trzy wektory wierszowe
% 2) trzy tablice komórkowe (cell arrays) o rozmiarze [1,4].
% node_counts - wektor zawierający liczby węzłów, dla których wyznaczana
%   była interpolacja wielomianowa
% exact_runge - wektor wierszowy wartości funkcji Runge wyznaczonych
%       w punktach x_fine = linspace(-1, 1, 1000);
% exact_sine - wektor wierszowy wartości funkcji sinusoidalnej wyznaczonych
%       w punktach x_fine = linspace(-1, 1, 1000);
% V{i}: macierz Vandermonde'a wyznaczona dla node_counts(i) węzłów interpolacji
% interpolated_runge{i}: wektor wierszowy wartości wielomianu interpolującego
%       funkcję Runge'go dla stopnia wielomianu równego node_counts(i)-1.
% interpolated_sine{i}: wektor wierszowy wartości wielomianu interpolującego
%       funkcję sinusoidalną dla stopnia wielomianu równego node_counts(i)-1.

% Oznaczonie TODO wskazuje linijki kodu wymagające zmian

    % Lista liczby węzłów interpolacyjnych do przetestowania
    node_counts = [2,4,8,16]; % TODO

    % Definicja funkcji Rungego
    runge_function = @(x) 1 ./ (1 + 25 * x.^2);
    % Definicja funkcji sinusoidalnej
    sine_function = @(x) sin(2 * pi * x);

    % Gęsta siatka punktów do testowania interpolacji
    x_fine = linspace(-1, 1, 1000);

    % Ilustracja wartości wzorcowych interpolowanych funkcji
    % Wartości funkcji Rungego w punktach testowych (wartości wzorcowe)
    exact_runge = runge_function(x_fine);
    % Wartości funkcji sinusoidalnej w punktach testowych (wartości wzorcowe)
    exact_sine = sine_function(x_fine);
    subplot(2,1,1);
    plot(x_fine, exact_runge, 'k--', 'LineWidth', 2, 'DisplayName',...
        'Wartości wzorcowe');
    hold on;
    subplot(2,1,2);
    plot(x_fine, exact_sine, 'k--' , 'LineWidth', 2, 'DisplayName',...
        'Wartości wzorcowe');
    hold on;

    for i = 1:length(node_counts)
        N = node_counts(i);
        % Węzły interpolacji równomiernie rozmieszczone na przedziale [-1, 1]
        x_nodes = linspace(-1, 1, N)';

        % wyznaczenie macierzy Vandermonde
        V{i} = get_vandermonde_matrix(x_nodes);

        % Obliczenie wartości funkcji w węzłach
        y_runge = runge_function(x_nodes);
        % Wyznaczenie wsp. wielomianu interpolacyjnego dla runge_function
        coefficients_runge = V{i}\y_runge; % TODO
        % odwrócenie kolejności wsp. wielomianów: dostosowanie do polyval
        coefficients_runge = coefficients_runge(end:-1:1);
        % Wyznaczenie wartości wielomianu w punktach testowych
        interpolated_runge{i} = polyval(coefficients_runge, x_fine);


        y_sine = sine_function(x_nodes); % TODO
        coefficients_sine = V{i}\y_sine; % TODO
        coefficients_sine = coefficients_sine(end:-1:1);
        interpolated_sine{i} = polyval(coefficients_sine, x_fine); % TODO

        subplot(2,1,1);
        % TODO: plot interpolated_runge{i} 
        plot(x_fine, interpolated_runge{i}, '--', 'LineWidth', 1, 'DisplayName',...
            ['Interpolacja, ', num2str(N), ' węzłów']);
        hold on;
        subplot(2,1,2);
        % TODO: plot interpolated_sine{i}
        plot(x_fine, interpolated_sine{i}, '--', 'LineWidth', 1, 'DisplayName',...
            ['Interpolacja, ', num2str(N), ' węzłów']);
        hold on;
    end

    % TODO: dodaj opisy wykresów oraz legendę
   subplot(2,1,1);
    title('Interpolacja funkcji Rungego');
    xlabel('x');
    ylabel('f(x)');
    legend('Location', 'best');
    
    subplot(2,1,2);
    title('Interpolacja funkcji sinusoidalnej');
    xlabel('x');
    ylabel('f(x)');
    legend('Location', 'best');


    set(gcf, 'Position', [1000 500 2000 1500]);
end

function V = get_vandermonde_matrix(x)
    % Buduje macierz Vandermonde’a na podstawie wektora węzłów interpolacji x.
    N = length(x);
    V = ones(N, N);
    for i = 1:N
        for j = 1:N
            V(i,j) = x(i) ^ (j - 1);
        end
    end
end