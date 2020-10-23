from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square
import requests
import pprint


def get_location_info():
    print("Получение информации по ip адресу")
    return requests.get("http://ip-api.com/json/").json()
    

def main():
    print("Выполнил: Дюжев Степан Андреевич ИУ5Ц-73Б")
    rect = Rectangle(73, 73, "blue")
    circle = Circle(73, "green")
    square = Square(73, "red")

    print(rect)
    print(circle)
    print(square)
    
    pprint.pprint(get_location_info())


if __name__ == "__main__":
    main()
