function velocity_delta = velocity_difference(t)
% t - czas od startu rakiety
if t <= 0
    msg = 'Time should be more or equal to 0';
    error(msg);
else
    u = 2000;
    m0 = 150000;
    q = 2700;
    g = 1.622;
    
    v = u*log(m0/(m0-(q*t)))-(g*t);
    M = 700;
    velocity_delta = v - M;
end

end