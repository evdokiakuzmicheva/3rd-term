clear
global fd;
fd = 44100;
T = 2;
%%
rec = audiorecorder(fd, 16, 1);
recordblocking(rec, T);
signal = getaudiodata(rec);
%%
signal = audioread('hight.wav');
%%
t = (0 : length(signal) - 1) / fd;

subplot(4, 1, 1)
plot(t, signal, '.-')
axis([0, T, 1.1*min(signal), 1.1*max(signal)])
title('signal')
%%
N = fix(log2(length(signal)));
x1 = signal(1 : 2^N);
X = fft(x1);
f = (0 : length(x1) - 1) * fd / length(x1);
subplot(4, 1, 2)
plot(f, abs(X), '.-')
axis([0, 1000, 0, 1.1*max(abs(X))])
title('spectr')
%%
audiowrite('input_hight.wav', signal, fd)
%%
Y = ffilt(X, 200);

subplot(4, 1, 3)
plot(f, abs(Y), '.-'); grid on
axis([0, 2000, 0, 1.1*max(Y)])
title('filted signal')
%%
filted_signal = ifft(Y);
subplot(4, 1, 4)
plot(t, signal, t(1 : length(filted_signal)), filted_signal, '.-'); grid on
title('2 signala')
%%
audiowrite('output_hight.wav', filted_signal, fd)
%%
sound(signal, fd)
%%
sound(filted_signal, fd)
%%
voice_frequences = main_fr(X, 50)