import os
from sys import exit
import matplotlib.pyplot as plt
import numpy as np

#adress = str(input()).split(' ')
adress = 'lab3_test.rtf'
for i in range(len(adress)):
    try:
        with open(os.path.join(adress)) as f:
            nums = f.read().splitlines()
    except:
        print('Error')
        exit()

def del_symbol(s):
    s = list(s)
    del s[len(s) - 1]
    s_ = ''
    for i in range(len(s)):
        s_ += s[i]
    return s_

for i in range(9):
    del nums[0]
for i in range(len(nums)):
    nums[i] = del_symbol(nums[i])
nums = np.matrix(np.array(nums, dtype = 'float64').reshape(len(nums), 1))

A = np.eye(len(nums)) - np.roll(np.eye(len(nums)), -1, axis=1)

N = np.arange(len(nums))
ax = plt.figure().add_subplot(111)
for i in range(255):
    nums -= np.dot(0.5 * A, nums)
    ax.plot(N, nums)
    ax.set(yticks = [0, 10])
    plt.title('N = ' + str(i + 1))
    plt.pause(0.02)
    ax.clear()
plt.show()
