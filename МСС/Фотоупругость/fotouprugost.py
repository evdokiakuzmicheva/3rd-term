import os
from sys import exit
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
g = 9.8
a1, a2, h, b = 140, 215, 29.8, 5.7

try:
    data = pd.ExcelFile('1-й опыт.xlsx').parse()
except:
    print('Error')
    exit()

delta_sigma_ = 0.001 * 30 * data['m, g'] * g * (a2 - a1) / (b * h ** 3) * data['delta y, mm']
delta_sigma = delta_sigma_.mean()

sr = round(abs(delta_sigma - delta_sigma_).mean(), 2)
sr_square = round(((abs(delta_sigma - delta_sigma_) ** 2).sum()) ** 0.5 / np.sqrt((len(delta_sigma_) - 1)), 2)
print('Сигма средняя:', round(delta_sigma, 2), '\tПогрешность:', sr, '\tСреднеквадратичная погрешность', sr_square)

try:
    data2 = pd.ExcelFile('2-й опыт.xlsx').parse()
except:
    print('Error')
    exit()

x = data2['x']
data2['sigma_x^2, delta_x'] /= 2
print(data2)
sigma1 = data2['sigma_x^1, delta_x'] * delta_sigma
sigma2 = data2['sigma_x^2, delta_x'] * delta_sigma

#x = np.array([0, 15, 35, 50, 65])
y = 15.61 - x * 0.145
fig, ax = plt.subplots()
ax.plot(x, y, '-', label = 'теор')

#ax.plot(x, sigma1, '.-', label = 'эксп1')
ax.plot(x, sigma2, '.-', label = 'эксп')

ax.set_xlabel('x, мм')
ax.set_ylabel('sigma, Н / мм^2')
ax.grid()
ax.legend()
plt.show()

print(len(x))
print('Погрешность:', round((delta_sigma * sr * x).mean(), 2), 'Н / мм^2')

sr_otklonenie = abs(sigma2 - y).mean()
print('Среднее отклонение', round(sr_otklonenie / y.mean() * 100), '%')
sr_square_otklonenie = (((sigma2 - y) ** 2).sum() / len(sigma2)) ** 0.5
print(print('Среднеквадратичное отклонение', round(sr_square_otklonenie / y.mean() * 100), '%'))
