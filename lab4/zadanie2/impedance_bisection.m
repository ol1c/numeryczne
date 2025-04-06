function [xvec,xdif,xsolution,ysolution,iterations] = impedance_bisection()
% Wyznacza miejsce zerowe funkcji impedance_difference metodą bisekcji.
% xvec - wektor z kolejnymi przybliżeniami miejsca zerowego, gdzie xvec(1)= (a+b)/2
% xdif - wektor różnic kolejnych przybliżeń miejsca zerowego
%   xdif(i) = abs(xvec(i+1)-xvec(i));
% xsolution - obliczone miejsce zerowe
% ysolution - wartość funkcji impedance_difference wyznaczona dla f=xsolution
% iterations - liczba iteracji wykonana w celu wyznaczenia xsolution

a = 1; % lewa granica przedziału poszukiwań miejsca zerowego
b = 10; % prawa granica przedziału poszukiwań miejsca zerowego
ytolerance = 1e-12; % tolerancja wartości funkcji w przybliżonym miejscu zerowym.
% Warunek abs(f1(xsolution))<ytolerance określa jak blisko zera ma znaleźć
% się wartość funkcji w obliczonym miejscu zerowym funkcji f1(), aby obliczenia
% zostały zakończone.
max_iterations = 1000; % maksymalna liczba iteracji wykonana przez alg. bisekcji

fa = impedance_difference(a);
fb = impedance_difference(b);

xvec = [];
xdif = [];
xsolution = Inf;
ysolution = Inf;
iterations = max_iterations;

for ii=1:max_iterations
    c = (a+b)/2;
    xvec(ii,1) = c;
    fc = impedance_difference(c);
    if(abs(fc)<ytolerance)
        xsolution = c;
        ysolution = fc;
        iterations = ii;
        break
    elseif (fa*fc) < 0
        b = c;
        fb = fc;
    else
        a = c;
        fa = fc;
    end
end

for i=1:iterations-1
    xdif(i,1) = abs(xvec(i+1)-xvec(i));
end

figure;
subplot(2,1,1);
plot(1:iterations, xvec);
title('Kolejne przybliżenia miejsca zerowego (skala liniowa)');
xlabel('iteracje');
ylabel('przybliżenia miejsca zerowego');

subplot(2,1,2);
semilogy(1:iterations-1, xdif);
title('Różnica pomiędzy kolejnymi przybliżeniami miejsca zerowego (skala logarytmiczna)');
xlabel('iteracje');
ylabel('różnica pomiędzy kolejnymi przybliżeniami');


end

function impedance_delta = impedance_difference (f)
% Tutaj wklej definicję funkcji zdefiniowanej w zadaniu 1.

if f <= 0
    msg = 'Frequency should be more or equal to 0';
    error(msg);
else
    R = 525;
    C = 0.00007;
    L = 3;
    absZ = 1 / sqrt((1/(R^2)) + ((2*pi*f*C) - (1/(2*pi*f*L)))^2 );
    M = 75;
    impedance_delta = absZ - M;
end

end