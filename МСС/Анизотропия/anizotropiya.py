import os
from sys import exit
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sympy import symbols, Eq, solve
from scipy import linalg

try:
    data = pd.ExcelFile('Анизотропия_new.xlsx').parse()
except:
    print('Error')
    exit()
for _ in data:
    try:
        _ = float(_)
    except:
        _ = str(_)
print(data)

rad = data['fi, grad'] * np.pi / 180
cos = round(np.cos(data['fi, grad'] * np.pi / 180), 2)
sigma = data['F, N'] / (data['h, mm'] * 2)

# solving system
i, j = 2, 5
fi_1, fi_2 = rad[i], rad[j]
f1, f2 = sigma[i] / sigma[0], sigma[j] / sigma[0]
b = np.array([-np.sin(fi_1) ** 4, -np.sin(fi_2) ** 4])
A = np.array([[np.cos(fi_1) ** 4 - 1 / f1 ** 2, np.sin(fi_1) ** 2 * np.cos(fi_1) ** 2],
              [np.cos(fi_2) ** 4 - 1 / f2 ** 2, np.sin(fi_2) ** 2 * np.cos(fi_2) ** 2]])

chi = np.sqrt(linalg.solve(A, b)[0])
b = linalg.solve(A, b)[1]

rad = np.linspace(start = 0, stop = np.pi / 2, num = 100)
theor = chi / np.sqrt(chi ** 2 * np.cos(rad) ** 4 + np.sin(rad) ** 4 + b * np.sin(rad) ** 2 * np.cos(rad) ** 2) * sigma[0]

fig, ax = plt.subplots()
ax.plot(cos, sigma, '.--', label = 'exp')
ax.plot(np.cos(rad), theor, '.--', label = 'theor')
ax.legend()
ax.set_title('sigma(cos(fi))')

plt.show()

rad = data['fi, grad'] * np.pi / 180
theor = chi / np.sqrt(chi ** 2 * np.cos(rad) ** 4 + np.sin(rad) ** 4 + b * np.sin(rad) ** 2 * np.cos(rad) ** 2) * sigma[0]
delta = abs(theor - sigma)
print('Среднее отклонение:\t', round(delta.sum() / len(delta) / theor.mean() * 100, 1), '%')
print('Среднеквадратичное отклонение:\t', round(np.sqrt((delta ** 2).sum()) / (len(delta) - 1) / theor.mean() * 100, 1), '%')
