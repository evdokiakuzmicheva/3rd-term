import os
from sys import exit
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

try:
      students_info = pd.ExcelFile('students/students_info.xlsx').parse()
      results_ejudge = pd.read_html('students/results_ejudge.html')[0]
except:
      print('Error')
      exit()

df = pd.merge(students_info, results_ejudge, left_on = 'login', right_on = 'User')
fig = plt.figure()
fig.add_subplot(1, 2, 1)
(df.groupby('group_out').mean().loc[:, 'Solved']).plot(kind = 'bar')
fig.add_subplot(1, 2, 2)
(df.groupby('group_faculty').mean().loc[:, 'Solved']).plot(kind = 'bar')
plt.show()

print(df[df['G'] > 10][df[df['G'] > 10]['H'] > 10]['group_faculty'],
      df[df['G'] > 10][df[df['G'] > 10]['H'] > 10]['group_out'])
