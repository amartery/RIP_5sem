class Color:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        """Цвет фигуры"""
        return self._color
