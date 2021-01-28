%% ��������� ������������� �������

T = 3;			% �������� ������������ ������������� �������
fd = 44100;		% ������� �������������
f = 5000;		% ������� ������������� �������

tt = linspace(0, T, T * fd);	        % �������� ������� �������
N = 2 ^ (nextpow2(length(tt)) - 1);     % ����������� ���������� ��������� (������������ �� ��������� ������� ������)
tt = tt(1:N);
ff = linspace(0, fd, N);				% ���ޣ� ������ ��������

%% ������������� �������
% �������� ������� �������
sz = size(tt);
% for i = 1:sz(2)
%     signal(i) = sin(2*pi*f*tt(i));   
% end
signal = sin(2*pi*f*tt);
subplot(6,1,1);
plot(tt,signal);grid on
%% ������������� ����
rng('default');
noise = randn(sz);
subplot(6,1,2);
plot(tt,noise);grid on
%% ������������� ������������ ������� � ����
for i = 1:length(tt)
    mix(i) = 0.1 * signal(i) + noise(i);		% �������� 0.1 * ������ + ���
end
subplot(6,1,3);
plot(tt,mix);grid on
%% ���������� ������� � ������
MIX = fft(mix);
l = length(mix);
f_ = (0 : l - 1) * fd / l;
subplot(6,1,4);
plot(f_,abs(MIX),'.-'); grid on
%% ���������� ����
MIX_filtered = MIX;
for i = 1 : length(tt)
    if (abs(MIX(i)) < 3000)
       MIX_filtered(i)=0;
    end
end
subplot(6,1,5);
plot(f_,abs(MIX_filtered),'.-'); grid on
%% �������������� �������
mix_filtered = ifft(MIX_filtered);
subplot(6,1,6);
plot(f_,mix_filtered,'.-'); grid on 