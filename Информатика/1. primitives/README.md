# primitives
Сначала надо задать size - размеры холста - в виде size = Point(…, …), цвет холста: color = ‘…’. Создать экземпляр класса window для создания холста, передать туда эти параметры: win = window(size, color).
### Класс polygone
На вход подается массив из точек типа Point и цвет. Для инициализации можно воспользоваться функцией init().
### Класс circle
На вход подаются параметры: радиус, координата центра по х, координата центра по у, цвет.
### Методы, применимые для классов polygone и circle.
Метод move_: принимает на вход расстояние l, на которое надо переместить объект; направление dir (в формате радиус вектора типа Point), в котором осуществлять движение; размеры холста size. При столкновении со стенкой холста элемент прекращает движение. Метод move_infinity: принимает на вход направление dir, размеры холста size. При столкновении со стенками объект упруго от них отражается. Методы S и P возвращают площадь и периметр фигуры соответственно. Метод is_in_figure принимает на вход точку в формате Point и возвращает True или False в зависимости от того, находится ли точка внутри или вне данного объекта. Методы S и is_in_figure работают только для выпуклых многоугольников.
### .
Функция regular_polygon принимает на вход точку center, радиус rad, N, цвет color и возвращает экземпляр класса polygone - правильный N-угольник с центром в точке center и радиусом описанной окружности rad.
### .
В конце написать root.mainloop()
