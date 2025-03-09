function plot_circles(a, b, circles)
    % Rysowanie prostokąta jako tło
    figure;
    rectangle('Position', [0, 0, a, b], 'EdgeColor', 'k', 'LineWidth', 2);
    hold on;
    
    % Ustawienia osi
    axis equal;
    axis([0 a 0 b]);
    
    % Rysowanie okręgów
    for i = 1:size(circles, 1)
        plot_circle(circles(i, 3), circles(i, 1), circles(i, 2));
        pause(0.1); 
    end
    
    hold off;
end
