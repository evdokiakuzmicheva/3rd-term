import os
from sys import exit
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('flights.csv', index_col = 0)
fig = plt.figure()
fig.add_subplot(1, 3, 1)
df.groupby('CARGO').sum().loc[:, 'WEIGHT'].plot(kind = 'bar', title = 'Total weight')
ax_2 = fig.add_subplot(1, 3, 2)
df.groupby('CARGO').count().loc[:, 'PRICE'].plot(kind = 'bar', title = 'Number of flights')
ax_3 = fig.add_subplot(1, 3, 3)
df.groupby('CARGO').sum().loc[:, 'PRICE'].plot(kind = 'bar', title = 'Total_price')
plt.show()
