import os
from sys import exit
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

try:
      data = pd.ExcelFile('Изгиб балки.xlsx').parse()
except:
      print('Error')
      exit()
data['Смещение'] -= 0.1


l = 67
a_, b_ = l / 2, l / 2
k1 = (3*a_ + 2*b_) / (a_ + b_) ** 3 * b_ ** 2
k2 = (k1 * (a_ + b_) ** 3 / 3 - (a_ * b_ ** 2 / 2 + b_ ** 3 / 3)) / (2 * 10 ** 6 * 0.714)
print(k1, k2)

fig, ax = plt.subplots(1, 3)

a1 = (data['P'] * data['R_B']).sum() / (data['P'] * data['P']).sum()

ax[0].plot(data['P'], data['R_B'], '.', label = 'exp')
ax[0].plot(data['P'], a1 * data['P'], '--', label = 'approx')
ax[0].plot(data['P'], k1 * data['P'], '--', label = 'theor')
ax[0].set_title('exp: R_B = ' + str(round(a1, 3)) + 'P\ntheor: R_B = ' + str(round(k1, 3)) + 'P')
ax[0].set_ylabel('R_B')
ax[0].set_xlabel('P')

# погрешность
delta = abs(k1 * data['P'] - a1 * data['P'])
sr_theor = (k1 * data['P']).sum() / (k1 * data['P']).size
sr_delta = delta.sum() / delta.size
sr_square = ((delta * delta).sum() / ((delta * delta).size)) ** 0.5
print('R_B(P):')
print('\tСреднеквадратичная погрешность:', str(round(sr_square / sr_theor * 100, 2)) + '%')
print('\tСреднее отклонение:', str(round(sr_delta / sr_theor * 100, 2)) + '%')

ax[1].plot(data['P'], data['Смещение'], '.', label = 'exp')
a2 = (data['P'] * data['Смещение']).sum() / (data['P'] * data['P']).sum()
ax[1].plot(data['P'], a2 * data['P'], '--', label = 'approx')
ax[1].plot(data['P'], k2 * data['P'], '--', label = 'theor')
ax[1].set_title('exp: l = ' + str(round(a2, 3)) + 'P\ntheor: l = ' + str(round(k2, 3)) + 'P')
ax[1].set_xlabel('P')
ax[1].set_ylabel('l')

# погрешность
delta = abs(k2 * data['P'] - a2 * data['P'])
sr_theor = (k2 * data['P']).sum() / (k2 * data['P']).size
sr_delta = delta.sum() / delta.size
sr_square = ((delta * delta).sum() / ((delta * delta).size)) ** 0.5
print('l(P):\t 1-й график')
print('\tСреднеквадратичная погрешность:', str(round(sr_square / sr_theor * 100, 2)) + '%')
print('\tСреднее отклонение:', str(round(sr_delta / sr_theor * 100, 2)) + '%')

k2 = (a1 * (a_ + b_) ** 3 / 3 - (a_ * b_ ** 2 / 2 + b_ ** 3 / 3)) / (2 * 10 ** 6 * 0.714)
ax[2].plot(data['P'], data['Смещение'], '.', label = 'exp')
a = (data['P'] * data['Смещение']).sum() / (data['P'] * data['P']).sum()
ax[2].plot(data['P'], a * data['P'], '--', label = 'approx')
ax[2].plot(data['P'], k2 * data['P'], '--', label = 'theor')
ax[2].set_title('exp: l = ' + str(round(a, 3)) + 'P\ntheor: l = ' + str(round(k2, 3)) + 'P')
ax[2].set_xlabel('P')
ax[2].set_ylabel('l')

# погрешность
delta = abs(k2 * data['P'] - a2 * data['P'])
sr_theor = (k2 * data['P']).sum() / (k2 * data['P']).size
sr_delta = delta.sum() / delta.size
sr_square = ((delta * delta).sum() / ((delta * delta).size)) ** 0.5
print('l(P):\t 2-й график')
print('\tСреднеквадратичная погрешность:', str(round(sr_square / sr_theor * 100, 2)) + '%')
print('\tСреднее отклонение:', str(round(sr_delta / sr_theor * 100, 2)) + '%')

for _ in ax:
    _.grid(linestyle = '--')
    _.legend()
plt.show()
