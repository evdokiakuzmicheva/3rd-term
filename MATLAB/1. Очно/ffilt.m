function [y] = ffilt(x, porog)
lx = length(x);
for i = 1 : lx
    if abs(x(i)) > porog
        y(i) = x(i);
    else
        y(i) = 0;
    end
end
end

