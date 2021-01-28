import os
import matplotlib.pyplot as plt
import numpy as np

#adress = str(input()).split(' ')
adress = 'signals/signal03.dat'
s = ''
array = []
for i in range(len(adress)):
    with open(os.path.join(adress)) as f:
        nums = f.read().splitlines()
    pass
    for j in range(len(nums)):
        array.append(nums[j])
for i in range(len(nums)):
    nums[i] = float(nums[i])

nums = np.array(nums)
C = np.cumsum((nums), dtype = 'float64')
A = np.zeros(C.size)

for i in range(10):
    A[i] = float(C[i] / (i + 1))
'''
for i in range(10, C.size):
    A[i] = (C[i] - C[i - 10]) / 10
    '''
A[10:] = (C[10:] - C[:-10]) / 10

N = np.arange(C.size)
fig, ax = plt.subplots(1, 2)  # Create a figure and an axes.
ax[0].plot(N, nums)  # Plot some data on the axes.
ax[1].plot(N, A)  # Plot more data on the axes...
ax[0].set_title("Raw signal")
ax[1].set_title("Filted signal")
ax[0].set_ylim(0, 30)
ax[1].set_ylim(0, 30)
plt.show()
