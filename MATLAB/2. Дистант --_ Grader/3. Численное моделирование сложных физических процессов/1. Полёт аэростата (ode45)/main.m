m=0.2;
v=1;
g=9.8;
k=0.01;
dt=1;
V=1;
t=0:dt:600;
v=zeros(size(t));
y=zeros(size(t));
T=300;
R=8.31;
M=0.029;
g=9.8;
rho=1;
rho=rho*exp((-M*g*y)/(R*T));
for i = 1: length(t) - 1
    rho=1;
    rho=rho*exp((-M*g*y(i))/(R*T));
    F_arch = g * V * rho;
    F_resist = -k *v(i);
    F_grav = -m*g;
    v(i+1) = v(i) + (F_arch + F_grav + F_resist)/ m*dt;
    y(i+1) = y(i) + v(i+1)*dt;
end

figure();
subplot(2, 2, 1)
plot(t,v,'.');
xlabel( 'Время, с');
ylabel( 'Скорость, м/с');
title('Скорость аэростата времени');
grid on;

subplot(2, 2, 2)
plot(t,y/1e3,'.');
xlabel( 'Время, с')
ylabel( 'Высота, км');
title( 'Высота аэростата времени');
grid on;

u0 = [0; 0];
[t_, u] = ode45(@fcn, [0 600], u0);
t = t_;
v = u(:, 2);
y = u(:, 1);
subplot(2, 2, 3)
plot(t_, '.');
xlabel('Номер шага');
ylabel('Шаг по времени, с');
title('Расчётная сетка');
grid on;

function dudt = fcn(t_, u)
    y = u(1);
    v = u(2);
    
    dudt = zeros(size(u));
    
    m = 0.2;
    V = 1;
    g = 9.8;
    k = 0.02;
    
    T = 300;
    R = 8.31;
    M = 0.029;
    g = 9.8;
    rho0 = 1;
    rho = rho0 * exp((-M * g * y) / (R * T));
    
    F_arch = g * V * rho;
    F_resist = -k * rho * v;
    F_grav = -m * g;
    
    dudt(1) = v;
    dudt(2) = (F_arch + F_resist + F_grav) / m;
end