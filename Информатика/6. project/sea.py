from random import randint
import numpy as np
from PIL import Image, ImageColor, ImageDraw, ImageFont
import pandas as pd

class Point:
    # 'X' - подбит, '.' - пустое поле, 'K' - корабль
    def __init__(self, x, y):
        self.x, self.y = x, y

width, height = 1200, 1200
column = [chr((np.arange(10) + 65)[i]) for i in range(0, 10)]
class board:
    def __init__(self):
        self.array = []
        null_string = ['O'] * 10
        for i in range(10):
            self.array.append(null_string)
        self.array = np.array(self.array)
        self.data = {}
        for i in range(10):
            self.data[column[i]] = self.array[i]
        self.data = pd.DataFrame(self.data, index = np.arange(1, 11))

    # случайное заполнение
    def placement(self):
        p = 0
        while p < 5:
            letter = column[randint(0, 9)]
            number = randint(1, 10)
            if self.data[letter][number] == 'O':
                self.data[letter][number] = 'X'
                p += 1
        p = 0
        while p < 3:
            letter = column[randint(0, 9)]
            number = randint(1, 10)
            if self.data[letter][number] == 'O':
                self.data[letter][number] = 'K'
                p += 1
        return

    def draw(self):
        numbers_X, numbers_Point, numbers_Board = Point([], []), Point([], []), Point([], [])
        for i in range(10):
            for j in range(1, 11):
                if self.data[column[i]][j] == 'X':
                    numbers_X.x.append(j)
                    numbers_X.y.append(column[i])
                elif self.data[column[i]][j] == 'O':
                    numbers_Point.x.append(j)
                    numbers_Point.y.append(column[i])
                elif self.data[column[i]][j] == 'K':
                    numbers_Board.x.append(j)
                    numbers_Board.y.append(column[i])
        if numbers_X.x != []:
            for i in range(len(numbers_X.x)):
                draw_field(numbers_X.x[i], numbers_X.y[i], 'flash')
        if numbers_Point.x != []:
            for i in range(len(numbers_Point.x)):
                draw_point(numbers_Point.x[i], numbers_Point.y[i])
        if numbers_Board.x != []:
            for i in range(len(numbers_Board.x)):
                draw_field(numbers_Board.x[i], numbers_Board.y[i], 'board')

def draw_point(i, j):
    i -= 1
    j = ord(j) - 65
    image = Image.open('current_board.jpg')
    draw = ImageDraw.Draw(image)
    point1 = Point(100 + j * 100, height - (100 * (i + 1) + 100))
    point2 = Point(point1.x + 100, point1.y + 100)
    draw.ellipse((point1.x + 35, point1.y + 35, point2.x - 35, point2.y - 35),
                 fill = 'blue',
                 outline = 'yellow',
                 width = 3)
    image.save("current_board.jpg")

def draw_field(i, j, s):
    i -= 1
    j = ord(j) - 65
    image = Image.open('current_board.jpg')
    point1 = Point(100 + j * 100, height - (100 * (i + 1) + 100))
    if s == 'flash':
        watermark = Image.open('materials/flash.png')
    elif s == 'board':
        watermark = Image.open('materials/board.png')
    image.paste(watermark, (point1.x, point1.y), watermark)
    image.save("current_board.jpg")

def create_empty_board():
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)

    for i in range(11):
        draw.line((100 * (i + 1), 100, 100 * (i + 1), height - 100))
        draw.line((100, 100 * (i + 1), width - 100, 100 * (i + 1)))

    for i in range(10):
        ImageDraw.Draw(image).text(
            (100 * (i + 1) + 25, height - 100),  # Coordinates
            column[i],  # Text
            (0, 255, 255),  # Color
            font = ImageFont.truetype("materials/font.ttf", 52)
        )
        ImageDraw.Draw(image).text(
            (100 - 65, 100 * (i + 1) + 25),  # Coordinates
            str(10 - i),  # Text
            (0, 255, 255),  # Color
            font = ImageFont.truetype("materials/font.ttf", 52) # Font and size of text
        )
    image.save("current_board.jpg")

b = board()
# размещение кораблей случайным образом
b.placement()
# печать таблицы данных состояния поля
print(b.data)
# создание пустого поля
create_empty_board()
b.draw()
