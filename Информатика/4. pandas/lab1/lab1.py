import os
from sys import exit
import numpy as np
import pandas as pd

df = pd.read_csv('transactions.csv', index_col = 0)

df_OK = df[df['STATUS'] == 'OK']
column_sum = np.array(df_OK['SUM'], dtype = 'int64')
column_sum.sort()
print('3 самых крупных платежа из реально проведённых: ',
      column_sum[len(df_OK) - 1], column_sum[len(df_OK) - 2], column_sum[len(df_OK) - 3])

umbrella = df_OK[df_OK['CONTRACTOR'] == 'Umbrella, Inc']
print('полная сумма реально проведённых платежей в адрес "Umbrella, Inc": ',
      sum(np.array(umbrella['SUM'], dtype = 'int64')))
