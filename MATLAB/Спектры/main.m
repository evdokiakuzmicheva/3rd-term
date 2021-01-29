% %%
% % signal_triangle
% fd = 44100;
% T = 6 * 10^(-3);
% %tau = 2.5 * 10^(-3);
% A = 0.7;
% 
% t = 0 : 1/fd : 3;
% x = [];
% 
% for i = 1 : length(t)
%     if t(i) - fix(t(i) / T) * T < T / 4
%         x(i) = (t(i) - fix(t(i) / T) * T) * 4 * A / T;
%     else
%         x(i) = 0;
%     end
%     
%     if t(i) - fix(t(i) / T) * T > 3 * T / 4
%         x(i) = (t(i) - fix(t(i) / T) * T - T) * 4 * A / T;
%     end
%     
%     if t(i) - fix(t(i) / T) * T < 3 * T / 4
%         if t(i) - fix(t(i) / T) * T > T / 4
%             x(i) = (- (t(i) - fix(t(i) / T) * T) + T / 2) * 4 * A / T; 
%         end
%     end
% end
% 
% plot(t, x);
% axis([0, 4*T, -A, A]); grid on
% % %%
% % signal_sin
% fd = 44100;
% T = 6 * 10^(-3);
% tau = 2.5 * 10^(-3);
% A = 0.7;
% 
% t = 0 : 1/fd : 3;
% x = [];
% 
% for i = 1 : length(t)
%     if t(i) - fix(t(i) / T) * T < T / 2
%         x(i) = abs(sin(pi*t(i) / T));
%     else
%         x(i) = 0;
%     end
% end

%%
% signal_square
fd = 44100;
T = 6 * 10^(-3);
tau = 2.5 * 10^(-3);
A = 0.7;
B = 0.1;

t = 0 : 1/fd : 3;
x = [];

for i = 1 : length(t)
    if t(i) - fix(t(i) / T) * T < tau
        x(i) = A;
    else
        x(i) = B;
    end
end
%%
subplot(6, 1, 1)
plot(t, x);
axis([0, 4*T, -A, 2*A]); grid on
title('Исходный сигнал')
%%
N = fix(log2(length(x)));
y = x(1 : 2^N);
X = fft(y);
f = (0 : length(X) - 1) * fd / length(y);
subplot(6, 1, 2)
plot(f, 1.5 * abs(X)); grid on
title('Спектр исходного сигнала')
%%
for i = 1 : 1000
    X(1, i) = 0;
end
subplot(6, 1, 3)
plot(f, 1.5 * abs(X)); grid on
title('Изменённый спектр исходного сигнала')

z = ifft(X);
subplot(6, 1, 4)
plot(t(1 : length(z)), z); grid on
axis([0, 4*T, -1, 1])
title('Сигнал, воссозданный по изменённому спектру')
%%
k = 1.5;
Y = ffilt_new(X, k);
subplot(6, 1, 6)
plot(f, abs(Y)); grid on
title('Спектр сигнала с увеличенной частотой')
%%
y = ifft(Y);
subplot(6, 1, 5)
plot(t(1 : length(y)), y); grid on
axis([0, 2*T, -1, 1])
title('Сигнал с увеличенной частотой')
