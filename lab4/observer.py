from abc import ABC, abstractmethod

"""
Наблюдатель — это поведенческий паттерн,
который позволяет объектам оповещать другие объекты
об изменениях своего состояния.
"""


class NotificationManager:  # Наблюдаемая система
    def __init__(self):
        self.__subscribers = set()  # При инициализации множество подписчиков задается пустым

    def subscribe(self, subscriber):
        # Для того чтобы подписать пользователя, он добавляется во множество подписчиков
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)  # Удаление подписчика из списка

    def notify(self, message):
        for subscriber in self.__subscribers:
            subscriber.update(message)  # Отправка уведомления всем подписчикам


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, message):  # Абстрактный наблюдатель задает метод update
        pass


class MessageNotifier(AbstractObserver):
    def __init__(self, name):
        self.__name = name

    def update(self, message):  # Конкретная реализация метода update
        print(f'{self.__name} received message!')


class MessagePrinter(AbstractObserver):
    def __init__(self, name):
        self.__name = name

    def update(self, message):  # Конкретная реализация метода update
        print(f'{self.__name} received message: {message}')


if __name__ == '__main__':
    notifier = MessageNotifier("MyNotifier")
    manager = NotificationManager()
    manager.subscribe(notifier)

    subscriber1 = MessagePrinter("subscriber1")
    subscriber2 = MessagePrinter("subscriber2")
    manager.subscribe(subscriber1)
    manager.subscribe(subscriber2)

    manager.notify("Hi!")

