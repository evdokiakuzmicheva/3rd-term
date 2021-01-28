function [y] = ffilt_new(x, k)
lx = length(x);
x1 = x(2 : lx/2);
x2 = x(lx : -1 : lx/2 + 2);
for i = 1 : lx/2 - 1
    if ceil(i/k) > lx/2 - 1
        y1(i) = 0;
        y2(i) = 0;
    else
        y1(i) = x1(ceil(i / k));
        y2(i) = x2(ceil(i / k));
    end
end
y = [x(1) y1 x(lx/2 + 1) y2(length(y2) : -1 : 1)];
end