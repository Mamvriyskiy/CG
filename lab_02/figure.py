"""
    Модуль для работы с изображением фигуры
"""

from math import sin, cos
import numpy as np

class Func:
    """
        Класс функции, заданной узлами
    """
    def __init__(self, x_list, y_list):
        self.x_list = x_list
        self.y_list = y_list


class Fish:
    """
        Класс изображения фигуры
    """
    def __init__(self):
        """
            Конструктор класса
        """

        self.big_circle = self.create_circle(20, 20)                              #внешний круг
        self.small_circle = self.create_circle(16, 16)                            #средний круг
        self.smaller_circle = self.create_circle(2, 2)                            #маленький круг

        self.first_line = self.create_line(1.52, 12.8, 1.52, 9.6);                #правая верхняя линия
        self.second_line = self.create_line(-1.52, -12.8, -1.52, -9.6);           #левая нижняя линия
        self.third_line = self.create_line(1.52, 12.8, -1.52, -9.6);              #праввая нидняя линия
        self.fourth_line = self.create_line(-1.52, -12.8, 1.52, 9.6);             #левая вернхняя линия
 
        self.first_smaller_circle = self.create_circle_center(18, 0, 2, 2)
        self.first_smaller_line = self.create_lines(-1, 0, 1, 17, 18, 19)

        self.second_smaller_circle = self.create_circle_center(-18, 0, 2, 2)
        self.second_smaller_line = self.create_lines(-17, -18, -19, 1, 0, -1)

        self.third_smaller_circle = self.create_circle_center(0, 18, 2, 2)
        self.third_smaller_line = self.create_lines(17, 18, 19, -1, 0, 1)

        self.fourth_smaller_circle = self.create_circle_center(0, -18, 2, 2)
        self.fourth_smaller_line = self.create_lines(1, 0, -1, -17, -18, -19)

        self.left_foot = self.create_foot(0, 0, -20, -32, -12, -32)               #левая нога
        self.right_foot = self.create_foot(0, 0, 20, -32, 12, -32)                #правая нога

        self.full = [self.big_circle, self.small_circle, self.smaller_circle, self.first_line, self.second_line, \
            self.third_line, self.fourth_line, self.first_smaller_circle, self.first_smaller_line, \
            self.second_smaller_circle, self.second_smaller_line, self.third_smaller_circle, \
            self.third_smaller_line, self.fourth_smaller_circle, self.fourth_smaller_line,\
                self.left_foot, self.right_foot]

        self.centre = Func([0], [0])
        self.full.append(self.centre)


    def reset(self):
        """
            Сброс
        """
        self.__init__()

    def create_lines(self, a, b, c, d, e, f):

        return Func([e, f, d, e, d, f], [b, c, a, b, c, a])


    def create_foot(self, a_x, a_y, b_x, b_y, c_x, c_y):
    
        return  Func([a_x, b_x, c_x, a_x], [a_y, b_y, c_y, a_y])

    def create_circle(self, large_sa, small_sa):
        """
            Создание эллипса (тело, голова фигуры)
        """
        circle = Func([], [])
        angles = np.linspace(0, 360, 360)

        for angle in angles:
            circle.x_list.append(large_sa * cos(np.radians(angle)))
            circle.y_list.append(small_sa * sin(np.radians(angle)))

        return circle


    def create_line(self, a, b, c, d):
        """
            Создание больший линий
        """
        return Func([a, b], [c, d])


    def create_circle_center(self, c_x, c_y, a, b):

        circle = self.create_circle(a, b)

        circle.x_list = [x - c_x for x in circle.x_list]
        circle.y_list = [y - c_y for y in circle.y_list]

        return circle


    def move(self, dx, dy):
        """
            Перенос изображения фигуры
        """
        for element in self.full:
            element.x_list = [x + dx for x in element.x_list]
            element.y_list = [y + dy for y in element.y_list]


    def scaling(self, kx, ky, xc, yc):
        """
            Масштабирвание изображения
        """
        for element in self.full:
            element.x_list = [x * kx + (1 - kx) * xc for x in element.x_list]
            element.y_list = [y * ky + (1 - ky) * yc for y in element.y_list]


    def rotate(self, phi, xc, yc):
        """
            Поворот изображения
        """
        phi = -phi
        for element in self.full:
            tmp_x = [x for x in element.x_list]
            element.x_list = [xc + (x - xc) * cos(np.radians(phi))
                              + (element.y_list[i] - yc) * sin(np.radians(phi))
                              for i, x in enumerate(element.x_list)]
            
            element.y_list = [yc - (tmp_x[i] - xc) * sin(np.radians(phi))
                              + (y - yc) * cos(np.radians(phi))
                              for i, y in enumerate(element.y_list)]
