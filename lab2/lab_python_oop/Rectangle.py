from lab_python_oop import GeometricalFigure
from lab_python_oop import Color


class Rectangle(GeometricalFigure.GeometricalFigure):
    """Rectangle"""
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = Color.Color(color)

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return "Название класса: {}\n" \
               "ширина: {}\n" \
               "высота: {}\n" \
               "цвет: {}\n" \
               "площадь: {}\n".format(self.__doc__, self.width,
                                      self.height, self.color.color,
                                      self.area())
