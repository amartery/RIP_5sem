from abc import ABC, abstractmethod


class GeometricalFigure(ABC):
    @abstractmethod
    def area(self):
        """Площадь геометрической фигуры """
