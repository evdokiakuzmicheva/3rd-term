%% Проверки функций физической модели

test_resistanceForce = resistanceForce([0; 1], 1, linspace(-pi, pi));
test_dissipationMomentum = dissipationMomentum(linspace(-1, 1), 1, 1);

test_y = [0 1 10 100];  % Высота
test_airDensity = airDensity(test_y);

test_m = 1;             % Масса
test_g = 9.8;           % Ускорение свободного падения
test_gravityForce = gravityForce(test_m, test_g);

test_mu = -20;          % Расход массы ракеты
test_vjet = [0; -2e4];  % Вектор скорости потока продуктов горения
test_jetForce = jetForce(test_mu, test_vjet);

test_jetForce_norm = 1; % Длина вектора реактивной силы
test_L = 70;            % Длина ракеты
test_beta = linspace(-0.01, 0.01);  % Углы отклонения вектора тяги
% test_jetMomentum = jetMomentum(test_jetForce_norm, test_L / 2, test_beta);

% Проверки численной модели в точке старта
test_fcn_u0 = fcn(0, [20e3; 0; 0; 0; 0; 0; 0]);     % Проверка сил в покое
test_fcn_u1 = fcn(0, [20e3; 0; 0; 0; 100; 0; 0]);   % Проверка сил при движении вверх
test_fcn_u2 = fcn(0, [20e3; 0; 0; 0; 0; 0; 0.1]);   % Проверка моментов сил вращении

%% Решение ode45
u0 = [20e3; 0; 0; 0; 0; 0; 0];
options = odeset('MaxStep', 1);
[t, u] = ode45(@fcn, [0 600], u0, options);
m = u(:, 1);        % первый столбец матрицы u
r = u(:, 2:3);      % матрица из второго и третьего столбца матрицы u
v = u(:, 4:5);      % матрица из четвёртого и пятого столбца матрицы u
alpha = u(:, 6);    % шестой столбец матрицы u
omega = u(:, 7);


%% Визуализация решения plot
subplot(2,3,1);
plot(t,[r(:,1)/1e3 r(:,2)/1e3]);
xlabel('Время, с');
ylabel('Расстояние, км');
title('Координаты ракеты');
grid on;
axis([0 600 -500 2500]);
set(gca, 'XTick', 0:200:600);
set(gca, 'YTick', -500:500:2500);
legend({'x','y'},'Location','northwest');

subplot(2,3,2);
plot(t,[v(:,1)/1e3 v(:,2)/1e3 sqrt(v(:,1).^2+v(:,2).^2)/1e3]);
xlabel('Время, с');
ylabel('Скорость, км/с');
title('Скорость ракеты');
grid on;
axis([0 600 0 10]);
set(gca, 'XTick', 0:200:600);
set(gca, 'YTick', 0:2:10);
legend({'V_x','V_y','|V|'},'Location','northwest');

subplot(2,3,3);
plot(r(:,1)/1e3, r(:,2)/1e3);
xlabel('Расстояние, км');
ylabel('Расстояние, км');
title('Траектория ракеты');
grid on;
axis([0 2.3134e+03 0 1000]);
set(gca, 'XTick', 0:500:2000);
set(gca, 'YTick', 0:200:1000);

subplot(2,3,4);
plot(t,alpha);
xlabel('Время, с');
ylabel('Угол, рад');
title('Ориентация ракеты');
grid on;
axis([0 600 0 1.5]);
set(gca, 'XTick', 0:200:600);
set(gca, 'YTick', 0:0.5:1.5);

subplot(2,3,5);
plot(t,omega*1e3);
xlabel('Время, с');
ylabel('Угловая скорость, рад/с');
title('Угловая скорость ракеты');
grid on;
axis([0 600 0 8]);
set(gca, 'XTick', 0:200:600);
set(gca, 'YTick', 0:2:8);

subplot(2,3,6);
plot(t, m/1e3);
xlabel('Время, с');
ylabel('Масса, кг');
title('Масса ракеты');
grid on;
axis([0 600 8 20]);
set(gca, 'XTick', 0:200:600);
set(gca, 'YTick', 8:2:20);




%% Функция физической модели fcn
function dudt = fcn(t, u)
    dudt = zeros(size(u));
    g = 9.8;
    L = 70;
    m = u(1);
    y = u(3);
    Vx = u(4);
    Vy = u(5);
    alfa = u(6);
    omega = u(7);
    
    mu(t<500) = -20;
    mu(t>=500) = 0;
    dudt(1) = mu;
    
    dudt(2) = Vx;
    dudt(3) = Vy;
    
    rho = airDensity(y);
    gamma = alfa - atan(Vx/Vy);
    F = resistanceForce([Vx; Vy], rho, abs(gamma)) + gravityForce(m,g);
    M = dissipationMomentum(omega, rho, L);
    if (t<500)
        vjet = getVjet(alfa, getBeta(t));
        F = F + jetForce(mu, vjet);
        M = M + jetMomentum(norm(jetForce(mu, vjet)), L/2, getBeta(t));
    end    
    
    % dVx/dt п╦ dVy/dt 
    dudt(4) = F(1)/m;
    dudt(5) = F(2)/m;
    
    % d(alfa)/dt
    dudt(6) = u(7);
    
    % d(omega)/dt
    dudt(7) = -M/(m*L.^2) *12;
end
%% Вспомогательные функции
function rho = airDensity(y)
% плотность от высоты
    T = 300;
    R = 8.31;
    M = 0.029;
    g = 9.8;
    rho0 = 1;
    rho = rho0 * exp((-M * g * y) / (R * T));
end

function F = gravityForce(m, g)
    F = [0; -m * g];
end

function F = resistanceForce(v, rho, gamma)
    gamma(gamma > pi) = 2 * pi - gamma(gamma > pi);

    k = zeros(size(gamma));
    k(gamma <= pi/4) = 1;
    k(gamma > pi/4 & gamma <= 3*pi/4) = 10;
    k(gamma > 3*pi/4) = 2;

    F = -v * norm(v) * k * rho * 10;
end

function F = jetForce(mu, vjet)
    F = [mu * vjet(1); mu * vjet(2)];
end

function M = dissipationMomentum(omega, rho, L)
    k = 500;
    M = k * omega * rho * L/2;
end

function vjet = getVjet(alfa, beta)
    S = S_matrix(-alfa-beta);
    vjet = S * [0; -20e3];
end

function beta = getBeta(t)
    beta(t < 80) = 0;
    beta(t >= 80 & t < 120) = -0.0001;
    beta(t >= 120 & t < 200) = 0;
    beta(t >= 200 & t < 240) = 0.00007;
    beta(t >= 240) = 0;
end

function S = S_matrix(fi)
    S = [cos(fi) -sin(fi);sin(fi)  cos(fi)];
end

function M = jetMomentum(jetForce_norm, l, beta)
    M = jetForce_norm * sin(beta) * l;
end