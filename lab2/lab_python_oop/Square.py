from lab_python_oop import Rectangle


class Square(Rectangle.Rectangle):
    """Square"""
    def __init__(self, a, color):
        super().__init__(a, a, color)

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return "Название класса: {}\n" \
               "длинна стороны: {}\n" \
               "цвет: {}\n" \
               "площадь: {}\n".format(self.__doc__, self.width,
                                      self.color.color, self.area())
