function [ft_5, integral_1000, Nt, integration_error] = trapezoidal_rule_accuracy_evaluation()
    % Funkcja służy do numerycznego obliczania całki oznaczonej metodą trapezów
    % z funkcji gęstości prawdopodobieństwa awarii urządzenia elektronicznego.
    % Jej celem jest porównanie dokładności obliczeń
    % w zależności od liczby zastosowanych podprzedziałów całkowania.
    %
    % ft_5 – wartość funkcji gęstości prawdopodobieństwa obliczona dla t = 5.
    %
    % integral_1000 – przybliżona wartość całki oznaczonej na przedziale [0, 5]
    %   wyznaczona metodą trapezów dla liczby podprzedziałów wynoszącej 1000.
    %
    % integration_error – wektor zawierający błędy bezwzględne numerycznego
    %   wyznaczenia wartości całki oznaczonej. Wartość integration_error(1,i)
    %   oznacza błąd obliczenia całki dla Nt(1,i) podprzedziałów:
    %   integration_error(1, i) = abs(integral_approximation - reference_value),
    %   gdzie reference_value to wzorcowa wartość całki.
    %
    % Nt – wektor wierszowy zawierający liczby podprzedziałów całkowania,
    %   dla których wyznaczane są przybliżenia całki i obliczany jest błąd.


    reference_value = 0.0473612919396179; % wartość wzorcowa całki

    ft_5 = failure_density_function(5);
    N = 1000; % liczba podprzedziałów całkowania
    x = linspace(0,5,N+1); % liczba punktów = liczba podprzedziałów całkowania + 1
    integral_1000 = trapezoidal_rule(x);

    Nt = 5:50:10^4;
    integration_error = zeros(1, length(Nt));
    for i=1:length(Nt)
        x = linspace(0,5,Nt(i)+1); % liczba punktów = liczba podprzedziałów całkowania + 1
        integration_error(i) = abs(trapezoidal_rule(x) - reference_value);
    end
    loglog(Nt, integration_error);
    xlabel("ilość przedziałów");
    ylabel("błąd");
    title("wartość błędu całkowania metodą trapezów");


end


function integral_approximation = trapezoidal_rule(x)
    % Oblicza przybliżoną wartość całki oznaczonej z funkcji gęstości
    % prawdopodobieństwa (failure_density_function) przy użyciu
    % metody trapezów.
    %
    % x – wektor rosnących wartości określających końce podprzedziałów całkowania.
    %     Dla n-elementowego wektora x zdefiniowanych jest n−1 podprzedziałów
    %     całkowania: [x(1), x(2)], [x(2), x(3)], ..., [x(n−1), x(n)].
    %
    % integral_approximation – przybliżona wartość całki oznaczonej


    trapezoids = (failure_density_function(x(1, 1:end-1)) + failure_density_function(x(1, 2:end))) ./ 2;
    delta = (x(end) - x(1)) / (length(x)-1);
    integral_approximation = sum(trapezoids) * delta;
end

function ft = failure_density_function(t)
    % Zwraca wartości funkcji gęstości prawdopodobieństwa wystąpienia awarii
    % urządzenia elektronicznego dla zadanych wartości czasu t.
    %
    % t – wektor wartości czasu (wyrażonych w latach), dla których obliczane
    %   są wartości funkcji gęstości prawdopodobieństwa.
    %
    % ft – wektor zawierający wartości funkcji gęstości prawdopodobieństwa
    %      odpowiadające kolejnym elementom wektora t.

    ft = 1/(3*sqrt(2*pi))*exp(-(t-10).^2/18);
end