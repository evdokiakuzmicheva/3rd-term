import os
import matplotlib.pyplot as plt

# Принимает на вход путь к месту, где лежит файл для тестирования
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
        a = 0

for i in range(9):
    del nums[0]

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
    nums[i] = nums[i].split(';')
    nums[i][1] = int(nums[i][1])
    nums[i][2] = int(nums[i][2])

preps, groups = set(), set()
for i in range(len(nums)):
    preps.add(nums[i][0])
    groups.add(nums[i][1])
preps, groups = list(preps), list(groups)
preps.sort()
groups.sort()

class para1:
    def __init__(self, prep, grades):
        self.prep = prep
        self.grades = grades

i = 0
preps_grades = []
for i in range(len(preps)):
    arr = []
    for j in range(len(nums)):
        if preps[i] == nums[j][0]:
            arr.append(nums[j][2])
    preps_grades.append(para1(preps[i], arr))

class para2:
    def __init__(self, grade, number):
        self.grade = grade
        self.number = number

# Возвращает распределение оценок по препу в процентах
def preps_grades_distribution(prep_grades):
    all_grades = []
    for i in range(3, 11):
        n = 0
        for j in range(len(prep_grades.grades)):
            if i == prep_grades.grades[j]:
                n += 1
        all_grades.append(para2(i, n))
    all_grades_procents = []
    for i in range(len(all_grades)):
        all_grades_procents.append(para2(all_grades[i].grade, 0))
        all_grades_procents[i].number = all_grades[i].number / len(prep_grades.grades)
        all_grades_procents[i].number *= 100
    return all_grades_procents
    # Если надо не в процентах, а в абсолютной величине, можно заменить на return all_grades

def name(i):
    if i == 3 or i == 4:
        s = 'уд'
    elif i <= 7:
        s = 'хор'
    else:
        s = 'отл'
    return s + ' ' + str(i)

# Можно раскомментировать и протестить оба фрагмента

'''
# 1
# Распределение по преподавателям для каждой оценки
fig, ax = plt.subplots()
x = ['3', '4', '5', '6', '7', '8', '9', '10']
ax = []
for i in range(len(preps)):
    p = preps_grades_distribution(preps_grades[i])
    data1 = []
    for j in range(len(p)):
        data1.append(p[j].number)
    ax.append(fig.add_subplot(2, 4, i + 1))
    ax[i].bar(x, data1, edgecolor = 'black', linewidth = 2)
    s = 'prep ' + str(i + 1)
    ax[i].set(title = s)
plt.show()
'''

'''
# 2
# Распределение по оценкам для каждого из преподавателей
fig, ax = plt.subplots()
x = []
for i in range(len(preps)):
    x.append(preps[i])

array = []
for i in range(len(preps)):
    array.append(preps_grades_distribution(preps_grades[i]))

data = []
for i in range(8):
    data.append([])
    for j in range(len(array)):
        data[i].append(array[j][i].number)
    if i == 0:
        ax.bar(x, data[i], label = name(i + 3))
    else:
        ax.bar(x, data[i], bottom = data[i - 1], label = name(i + 3))
    ax.legend()

plt.show()
'''
