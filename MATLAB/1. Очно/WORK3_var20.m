function [IM1] = WORK3_var20(IM, max_p)
p = 100;
sz = size(IM);
m = sz(1);
n = sz(2);
IM1(m, n, 3) = 0;
d = sqrt(m^2 + n^2);
for i = 1 : m
    for j = 1 : n
        r = sqrt(i^2 + j^2);
        p = max_p * abs(1 - 2 * r / d);
        if r < d / 2
            IM1(i, j, :) = (100 - p) / 100 * IM(i, j, :);
        else
            IM1(i, j, :) =  p / 100 + (100 - p) / 100 * IM(i, j, :);
        end
%         s = m / n * j - i;
%         p = max_p / m * s;
%         if s > 0
%             IM1(i, j, :) = (100 - p) / 100 * IM(i, j, :);
%         else
%             IM1(i, j, :) =  p / 100 + (100 - p) / 100 * IM(i, j, :);
%         end
    end
end
end