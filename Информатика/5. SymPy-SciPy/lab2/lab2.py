import os
from sys import exit
import numpy as np
from scipy import linalg
from matplotlib import pyplot as plt

adress = 'large.txt'
for i in range(len(adress)):
    try:
        with open(os.path.join(adress)) as f:
            nums = f.read().splitlines()
    except:
        print('Error')
        exit()

N = int(nums[0])
array = []
for i in range(1, len(nums)):
    nums[i] = nums[i].split(' ')
    if i != len(nums) - 1:
        array.append(nums[i])
    else:
        b = np.array(nums[i], dtype = 'float')
A = np.array(array, dtype = 'float')

print(linalg.solve(A, b))

fig, ax = plt.subplots()
values = linalg.solve(A, b)
ax.bar(np.arange(N), values)
ax.grid()
plt.show()
