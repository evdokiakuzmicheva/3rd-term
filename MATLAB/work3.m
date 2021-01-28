g = 9.8;
y0 = 25;
v0 = 30;
dt = 0.1;
t = 0 : dt : 10;

v = v0 + cumsum(repmat(-g, size(t)) * dt);
y = y0 + cumsum(v * dt);

y_kin = y0 + v0 * t - g * t .^ 2 / 2;

subplot(2, 1, 1)
plot(t, v, '.')
xlabel('�����, �')
ylabel('��������, �/�')
grid on
legend()
hold off
title('�������� �������� ��������� ����')

subplot(2, 1, 2)
plot(t, y, '.', 'DisplayName', '������������ ������')
hold on
plot(t, y_kin, '.', 'DisplayName', '�������������� ������')
xlabel('�����, �')
ylabel('��������, �/�')
grid on
legend()
hold off
title('������ �������� ��������� ����')