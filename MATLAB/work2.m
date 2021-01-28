g = 9.8;
y0 = 25;
v0 = 30;
dt = 0.1;
t = 0 : dt : 10;
y = y0 + v0 * t - g * t .^2 / 2;
y_max = max(y);
plot(t, y, '.'); grid on
xlabel('�����, �')
ylabel('������, �')
s1 = '����������� ������ �������� ��������� ���� �� �������';
s2 = '������������ ������ y_{max} = ';
s3 = string(y_max);
s = [s1 s2 s3];
s = s(1) + newline + s(2) + s(3);
title(s);