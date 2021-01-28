clear
fd = 44100;
T = 5 * 10^(-3);
tau = 0.75 * 10^(-3);
A = 0.7;
k = 2.2;

t = 0 : 1/fd : 3;
x = [];
for i = 1 : length(t)
    if t(i) - fix(t(i) / T) * T < tau
        x(i) = A;
    else
        x(i) = -A * tau / (T - tau);
    end
end
subplot(4, 1, 1)
plot(t, x); grid on
axis([0 4*T 4*min(x) 1.5*max(x)])
title('Исходный сигнал')
%%
N = fix(log2(length(x)));
y = x(1 : 2^N);
t1 = [];
X = fft(y);
f = ((0 : length(X) - 1) * fd / length(y));
subplot(4, 1, 2)
plot(f, 1.5*abs(X)); grid on
title('Исходный спектр')
%%
Y = ffilt_new(X, k);
subplot(4, 1, 4)
plot(f, abs(Y)); grid on
title('Спектр с увеличенной частотой')
%%
y = ifft(Y);
subplot(4, 1, 3)
plot(t(1 : length(y)), y); grid on
axis([0 4*T 1.5*min(y) 1.5*max(y)])
title('Сигнал с увеличенной частотой')