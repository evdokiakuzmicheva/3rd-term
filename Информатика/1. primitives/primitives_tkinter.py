from tkinter import *
from math import *

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

# Создание холста
class window:
    def __init__(self, size, color):
        global c, root
        root = Tk()
        c = Canvas(root, width = size.x, height = size.y, bg = color)
        c.pack()

# Инициализация массива точек
def init():
    array = []
    N = int(input())
    for i in range(N):
        array.append(str(input()).split(' '))
    for i in range(len(array)):
        array[i] = Point(int(array[i][0]), int(array[i][1]))
    return array

def sum(array, par):
    sum_ = 0
    for i in range(len(array)):
        if par == 'x':
            sum_ += array[i].x
        else:
            sum_ += array[i].y
    return sum_

def hyp(a, b):
    return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

# Площадь треугольника
def s_triangle(point1, point2, point3):
    p = (hyp(point1, point2) + hyp(point3, point2) + hyp(point1, point3)) / 2
    return sqrt(p * (p - a1) * (p - a2) * (p - a3))

class polygone:
    def __init__(self, array, color):
        self.array, self.color = array, color
        p = []
        for i in range(len(array)):
            p.append(array[i].x)
            p.append(array[i].y)
        self.obj = c.create_polygon(p, fill = self.color, outline = 'black')
        self.center_x, self.center_y = sum(array, 'x') / len(array), sum(array, 'y') / len(array)
        self.l, self.dir, self.size, self.start = 0, Point(0, 0), Point(0, 0), Point(0, 0)

    # определение центра массс многоугольника
    def centr(self):
        return Point(sum(self.array, 'x') / len(self.array), sum(self.array, 'y') / len(self.array))

    # Самая левая, правая, нижняя, верхняя координаты многоугольника
    def min_max(self):
        x, y = [], []
        for i in range(len(self.array)):
            x.append(self.array[i].x)
            y.append(self.array[i].y)
        return [min(x), max(x), min(y), max(y)]

    def move__(self):
        norm = sqrt(self.dir.x ** 2 + self.dir.y ** 2)
        self.speed = Point((5 * self.l / abs(self.l)) * (self.dir.x / norm), 5 * self.l / abs(self.l) * (self.dir.y / norm))
        self.center_x += self.speed.x
        self.center_y += self.speed.y
        for i in range(len(self.array)):
            self.array[i].x += self.speed.x
            self.array[i].y += self.speed.y
        # При столкновении со стенкой объект останавливается
        if self.min_max()[0] <= 0 or self.min_max()[1] >= self.size.x or self.min_max()[2] <= 0 or self.min_max()[3] >= self.size.y:
            return
        if (self.center_x - self.start.x) ** 2 + (self.center_y - self.start.y) ** 2 < self.l ** 2:
            root.after(100, self.move__)
        c.move(self.obj, self.speed.x, self.speed.y)

    # Движение на заданное расстояние l в заданном направлении dir
    def move_(self, l, dir, size):
        self.l, self.dir, self.size = l, dir, size
        self.start = Point(self.center_x, self.center_y)
        self.move__()

    def move_infinity_(self):
        norm = sqrt(self.dir.x ** 2 + self.dir.y ** 2)
        self.speed = Point((-5) * (self.dir.x / norm), (-5) * (self.dir.y / norm))
        c.move(self.obj, self.speed.x, self.speed.y)
        self.center_x += self.speed.x
        self.center_y += self.speed.y
        for i in range(len(self.array)):
            self.array[i].x += self.speed.x
            self.array[i].y += self.speed.y
        if self.min_max()[0] <= 0 or self.min_max()[1] >= self.size.x:
            self.dir.x *= -1
        if self.min_max()[2] <= 0 or self.min_max()[3] >= self.size.y:
            self.dir.y *= -1
        root.after(100, self.move_infinity_)

    # Бесконечное движение в заданном направлении dir
    def move_infinity(self, dir, size):
        self.dir, self.size = dir, size
        self.move_infinity_()

    # Площадь, если многоугольник выпуклый
    def S(self):
        S = 0
        for i in range(1, len(self.array) - 1):
            S += s_triangle(array[0], array[i], array[i + 1])
        return S

    # Периметр
    def P(self):
        P = 0
        for i in range(len(self.array) - 1):
            P += hyp(self.array[i], self.array[i - 1])
        P += hyp(self.array[0], self.array[len(self.array) - 1])
        return P

    # Показывает, находится ли данная точка внутри данного объекта
    def is_in_figure(self, point):
        S = 0
        for i in range(len(self.array) - 1):
            S += s_triangle(point, self.array[i], self.array[i + 1])
        if abs(S - self.S) > 1:
            return False
        return True

class circle:
    def __init__(self, rad, center_x, center_y, color):
        self.rad, self.center_x, self.center_y = rad, center_x, center_y
        self.l, self.dir, self.speed, self.size = 0, Point(0, 0), Point(0, 0), Point(0, 0)
        self.start = Point(self.center_x, self.center_y)
        self.obj = c.create_oval(self.center_x - self.rad, self.center_y - self.rad, self.rad + self.center_x, self.rad + self.center_y, fill = color, outline = 'black')

    def move__(self):
        norm = sqrt(self.dir.x ** 2 + self.dir.y ** 2)
        self.speed = Point((5 * self.l / abs(self.l)) * (self.dir.x / norm), 5 * self.l / abs(self.l) * (self.dir.y / norm))
        c.move(self.obj, self.speed.x, self.speed.y)
        self.center_x += self.speed.x
        self.center_y += self.speed.y
        # При столкновении со стенкой круг останавливается
        if self.center_x >= self.size.x - self.rad or self.center_x <= self.rad or self.center_y >= self.size.y - self.rad or self.center_y <= self.rad:
            return
        if (c.coords(self.obj)[1] + self.rad - self.start.x) ** 2 + (c.coords(self.obj)[3] - self.rad - self.start.y) ** 2 < self.l ** 2:
            root.after(100, self.move__)

    # Движение на заданное расстояние l в заданном направлении dir
    def move_(self, l, dir, size):
        self.l, self.dir, self.size = l, dir, size
        self.start = Point(self.center_x, self.center_y)
        self.move__()

    def move_infinity_(self):
        norm = sqrt(self.dir.x ** 2 + self.dir.y ** 2)
        self.speed = Point(5 * (self.dir.x / norm), 5 * (self.dir.y / norm))
        c.move(self.obj, self.speed.x, self.speed.y)
        self.center_x += self.speed.x
        self.center_y += self.speed.y
        if self.center_x >= self.size.x - self.rad or self.center_x <= self.rad:
            self.dir.x *= -1
        if self.center_y >= self.size.y - self.rad or self.center_y <= self.rad:
            self.dir.y *= -1
        root.after(100, self.move_infinity_)

    # Бесконечное движение в заданном направлении dir
    def move_infinity(self, dir, size):
        self.dir, self.size = dir, size
        self.move_infinity_()
        return

    # Площадь
    def S(self):
        return pi * self.rad ** 2

    # Периметр
    def P(self):
        return 2 * pi * self.rad

    # Показывает, находится ли данная точка внутри круга
    def is_in_figure(self, point):
        if (point.x - self.centr_x) ** 2 + (point.y - self.centr_y) ** 2 <= self.rad ** 2:
            return True
        return False

# Поворот точки point относительно точки center на угол angle
def rotate(point, center, angle):
    X = center.x + (point.x - center.y) * cos(angle) - (point.y - center.y) * sin(angle)
    Y = center.y + (point.y - center.y) * cos(angle) + (point.x - center.x) * sin(angle)
    return Point(X, Y)

# Возвращает экземпляр класса polygone - правильный выпуклый N-угольник с центром в точке center, с радиусом rad, цвета color
def regular_polygon(center, rad, N, color):
    array = []
    point = Point(center.x + rad, center.y)
    array.append(point)
    angle = 2 * pi / N
    for i in range(N):
        point = rotate(point, center, angle)
        array.append(point)
    return polygone(array, color)
'''
# ПРИМЕР ДЛЯ ТЕСТИРОВАНИЯ
size = Point(300, 300)
color = 'white'
win = window(size, color)
cr = circle(50, 150, 150, 'yellow')
#cr.move_(200, Point(1, 1), size)
cr.move_infinity(Point(2, 1), size)
#array = init()
array = [Point(50, 232), Point(143, 164), Point(263, 230), Point(139, 49)]
pol1 = polygone(array, 'green')
pol = regular_polygon(Point(100, 100), 50, 10, 'purple')
#pol.move_(-100, Point(1, 1), size)
pol.move_infinity(Point(-1, 1), size)
root.mainloop()
'''
