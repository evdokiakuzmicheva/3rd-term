import os
from sys import exit
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

try:
    data = pd.ExcelFile('Устойчивость.xlsx').parse()
except:
    print('Error')
    exit()
for _ in data:
    try:
        _ = int(_)
    except:
        _ = str(_)
#data = data.fillna(0)
print(data)

fig, ax = plt.subplots(1, 3)

fig.suptitle('1-я балка\nЗависимость P / P_cr от смещения', fontfamily = 'fantasy')
ax[0].plot(data['x1, мм'], data['P1, Н'] / data['P1, Н'].max(), '.')
ax[0].set_title('l = '+ str(data['l, см'][0]) + ' см')

ax[1].plot(data['x2, мм'], data['P2, Н'] / data['P2, Н'].max(), '.')
ax[1].set_title('l = ' + str(data['l, см'][1]) + ' см')

ax[2].plot(data['x3, мм'], data['P3, Н'] / data['P3, Н'].max(), '.')
ax[2].set_title('l = ' + str(data['l, см'][2]) + ' см')

for _ in ax:
    _.set_xlabel('y, мм')
    _.grid()

fig, ax = plt.subplots(1, 3)
fig.suptitle('2-я балка\nЗависимость P / P_cr от смещения', fontfamily = 'fantasy')
ax[0].plot(data['x4, мм'], data['P4, Н'] / data['P4, Н'].max(), '.')
ax[0].set_title('l = ' + str(data['l, см'][3]) + ' см')

ax[1].plot(data['x5, мм'], data['P5, Н'] / data['P5, Н'].max(), '.')
ax[1].set_title('l = ' + str(data['l, см'][4]) + ' см')

ax[2].plot(data['x6, мм'], data['P6, Н'] / data['P6, Н'].max(), '.')
ax[2].set_title('l = ' + str(data['l, см'][5]) + ' см')

for _ in ax:
    _.set_xlabel('y, мм')
    _.grid()

n = np.array([data['P1, Н'].max(),
              data['P2, Н'].max(),
              data['P3, Н'].max(),
              data['P4, Н'].max(),
              data['P5, Н'].max(),
              data['P6, Н'].max()
              ])

def trunc(x):
    part = x-int(x)
    if x >= 1:
        Fpart=round(part,2)
        return Fpart
    else:
        return x

def mean(numbers):
    t = round(trunc(numbers.mean()), 1)
    if t <= 0.2:
        t = 0
    elif t <= 0.7:
        t = 0.5
    else:
        t = 1
    return int(numbers.mean()) + t

fig, ax = plt.subplots(1, 2)

n1 = n[:3]
m1 = 10 ** 4 * data['l, см'][:3] ** (-2)
p1 = (n1 * m1).sum() / (m1 ** 2).sum()

c = 200 * 10 ** 9 * 2.26 * 10 ** (-12) * np.pi ** 2
numbers = 0.01 * data['l, см'][:6] * np.sqrt(n / c)
theor = c * mean(numbers[:3]) ** 2 / data['l, см'][:3] ** 2 * 10 ** 4

ax[0].plot(10 ** 4 * data['l, см'][:3] ** (-2), n[:3], '.', label = 'exp')
ax[0].plot(10 ** 4 * data['l, см'][:3] ** (-2), p1 * 10 ** 4 * data['l, см'][:3] ** (-2), '--', label = 'аппрокс')
ax[0].set_title('1-я балка\nэксп: P_кр = ' + str(round(p1, 2)) + ' * 1/l^2\nтеор: P_кр = ' + str(round(c * mean(numbers[:3]) ** 2, 2)) + ' * 1/l^2')
ax[0].plot(10 ** 4 * data['l, см'][:3] ** (-2), theor, '.--', label = 'theor')

delta = abs(n[:3] - theor)
print('1-я балка:')
print('\tСреднее отклонение: ', round(delta.sum() / len(delta) / theor.mean() * 100), '%')
print('\tСреднеквадратичное отклонение: ', round(np.sqrt((delta ** 2).sum()) / (len(delta) - 1) / theor.mean() * 100), '%')

c = 200 * 10 ** 9 * 2.95 * 10 ** (-12) * np.pi ** 2
numbers = 0.01 * data['l, см'][:6] * np.sqrt(n / c)
theor = c * mean(numbers[3:6]) ** 2 / data['l, см'][3:6] ** 2 * 10 ** 4

n2 = n[3:6]
m2 = 10 ** 4 * data['l, см'][3:6] ** (-2)
p2 = (n2 * m2).sum() / (m2 ** 2).sum()

ax[1].plot(10 ** 4 * data['l, см'][3:6] ** (-2), n[3:6], '.', label = 'exp')
ax[1].plot(10 ** 4 * data['l, см'][3:6] ** (-2), p2 * 10 ** 4 * data['l, см'][3:6] ** (-2), '--', label = 'approx')
ax[1].set_title('2-я балка\nэксп: P_кр = ' + str(round(p2, 2)) + ' * 1/l^2\nтеор: P_кр = ' + str(round(c * mean(numbers[3:6]) ** 2, 2)) + ' * 1/l^2')
ax[1].plot(10 ** 4 * data['l, см'][3:6] ** (-2), theor, '.--', label = 'theor')

delta = abs(n[3:6] - theor)
print('2-я балка:')
print('\tСреднее отклонение: ', round(delta.sum() / len(delta) / theor.mean() * 100), '%')
print('\tСреднеквадратичное отклонение: ', round(np.sqrt((delta ** 2).sum()) / (len(delta) - 1) / theor.mean() * 100), '%')

for _ in ax:
    _.grid()
    _.set_xlabel('l^(-2), м^(-2)')
    _.set_ylabel('P_кр, Н')
    _.legend()
#plt.show()

