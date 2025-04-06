function impedance_delta = impedance_difference(f)
% Wyznacza moduł impedancji równoległego obwodu rezonansowego RLC pomniejszoną o wartość M.
% f - częstotliwość
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