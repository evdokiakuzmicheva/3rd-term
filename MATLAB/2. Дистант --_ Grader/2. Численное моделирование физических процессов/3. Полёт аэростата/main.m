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
subplot(2, 1, 1) 
plot(t,v,'.'); 
xlabel( 'Время, с'); 
ylabel( 'Скорость, м/с'); 
title('Скорость аэростата от времени'); 
grid on;
subplot(2, 1, 2) 
plot(t,y/1e3,'.');
xlabel( 'Время, с') 
ylabel( 'Высота, км'); 
title( 'Высота аэростата от времени'); 
grid on;