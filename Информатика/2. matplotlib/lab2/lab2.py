import os
import matplotlib.pyplot as plt

# Считывает путь к месту, где лежит файл для тестирования
adress = str(input()).split(' ')
array = []
for i in range(len(adress)):
    try:
        with open(os.path.join(adress[i])) as f:
            nums = f.read().splitlines()
        pass
        for j in range(len(nums)):
            array.append(nums[j])
    except:
        print('File not found')

for i in range(9):
    del nums[0]
N = int(len(nums) / 2)

def delete_last_letter(s):
    arr = []
    for i in range(len(s)):
        arr.append(s[i])
    del arr[len(arr) - 1]
    s = ''
    for i in range(len(arr)):
        s += arr[i]
    return s

for i in range(len(nums)):
    nums[i] = delete_last_letter(nums[i])
for i in range(len(nums)):
    nums[i] = nums[i].split(' ')
    for j in range(len(nums[i])):
        nums[i][j] = float(nums[i][j])

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

def min_max(nums, s):
    arr, arr_min, arr_max = [], [], []
    if s == 'x':
        for i in range(len(nums)):
            if i % 2 == 0:
                arr.append(nums[i])
    elif s == 'y':
        for i in range(len(nums)):
            if i % 2 == 1:
                arr.append(nums[i])
    for i in range(len(arr)):
        arr_min.append(min(arr[i]))
        arr_max.append(max(arr[i]))
    return Point(min(arr_min), max(arr_max))

def decomposition(N):
    arr = []
    for i in range(1, int(N / 2) + 1):
        if N % i == 0:
            arr.append(i)
    arr.append(N)
    return arr

def division(N):
    arr = decomposition(N)
    return Point(arr[int(len(arr) / 2)], arr[int(len(arr) / 2) - 1])

fig = plt.figure()
i, j, ax = 0, 0, []
while i < 2 * N:
    if i % 2 == 0 and i < 2 * N - 1:
        j += 1
        ax.append(fig.add_subplot(division(N).x, division(N).y, j))
        ax[j - 1].plot(nums[i], nums[i + 1])
        ax[j - 1].set(xticks = [min_max(nums, 'x').x, min_max(nums, 'x').y], yticks = [min_max(nums, 'y').x, min_max(nums, 'y').y])
    i += 2

plt.show()
