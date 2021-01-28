clear variables;

u0 = [0; 0];
[t, u] = ode45(@fcn, [0 600], u0);
y = u(:, 1);
v = u(:, 2);

figure();
subplot(2, 2, 2);
plot(t, v, '.');
xlabel('Время, с');
ylabel('Скорость, м/с');
title('Скорость аэростата от времени');
grid on;

subplot(2, 2, 3);
plot(t, y / 1e3, '.');
xlabel('Время, с');
ylabel('Высота, м/с');
title('Высота аэростата от времени');
grid on;

subplot(2, 2, 1);
plot(t, '.');
xlabel('Номер шага');
ylabel('Шаг по времени, с');
title('Расчётная сетка');
grid on;

function dudt = fcn(t, u)
    y = u(1);
    v = u(2);
    
    dudt = zeros(size(u));
    
    m = 0.2;
    V = 1;
    g = 9.8;
    k = 0.02;
    
    F_arch = g * V * airDensity(y);
    F_resist = -k * airDensity(y) * v;
    F_grav = -m * g;
    
    dudt(1) = v;
    dudt(2) = (F_arch + F_resist + F_grav) / m;
end