from lab_python_oop import GeometricalFigure
from lab_python_oop import Color
import math


class Circle(GeometricalFigure.GeometricalFigure):
    """Circle"""
    def __init__(self, radius, color):
        self.radius = radius
        self.color = Color.Color(color)

    def area(self):
        return 2 * math.pi * self.radius

    def __repr__(self):
        return "Название класса: {}\n" \
               "радиус: {}\n" \
               "цвет: {}\n" \
               "площадь: {}\n".format(self.__doc__, self.radius,
                                      self.color.color, self.area())
