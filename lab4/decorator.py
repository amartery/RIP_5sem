from abc import ABC, abstractmethod

"""
Декоратор — это структурный паттерн, 
который позволяет добавлять объектам новые поведения на лету,
помещая их в объекты-обёртки.
"""


class Creature(ABC):
    @abstractmethod
    def feed(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def make_noise(self):
        pass


class Animal(Creature):
    def feed(self):
        print("I eat grass")

    def move(self):
        print("I walk forward")

    def make_noise(self):
        print("WOOO!")


class AbstractDecorator(Creature):
    def __init__(self, obj):
        self.obj = obj

    def feed(self):
        self.obj.feed()

    def move(self):
        self.obj.move()

    def make_noise(self):
        self.obj.make_noise()


class Swimming(AbstractDecorator):
    def move(self):
        print("I swim")

    def make_noise(self):
        print("...")


class Flying(AbstractDecorator):
    def move(self):
        print("I fly")

    def make_noise(self):
        print("QUAAA!")


class Predator(AbstractDecorator):
    def feed(self):
        print("I eat other animals")


class Fast(AbstractDecorator):
    def move(self):
        self.obj.move()
        print("Fast!")


if __name__ == '__main__':
    print("Базовое животное")
    animal = Animal()
    animal.feed()
    animal.move()
    animal.make_noise()
    print()

    print("Водоплавающее животное")
    animal = Swimming(animal)
    animal.feed()
    animal.move()
    animal.make_noise()
    print()

    print("Хищное животное")
    animal = Predator(animal)
    animal.feed()
    animal.move()
    animal.make_noise()
    print()

    print("Добавим хищнику скорости")
    animal = Fast(animal)
    animal.feed()
    animal.move()
    animal.make_noise()
    print()

    print("Еще раз добавим хищнику скорости(декораторы можно комбинировать)")
    animal = Fast(animal)
    animal.feed()
    animal.move()
    animal.make_noise()
    print()

