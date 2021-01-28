import os
import matplotlib.pyplot as plt
import sys

# Считывает путь к месту, где лежит файл для тестирования
adress = str(input()).split(' ')
s = ''
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
        sys.exit()

N = int(array[0])
for i in range(1, N + 1):
    array[i] = array[i].split(' ')

x, y = [], []
for i in range(1, N + 1):
    x.append(float(array[i][0]))
    y.append(float(array[i][1]))

plt.plot(x, y, '.')
plt.title('Number of points: ' + str(N))
plt.show()
