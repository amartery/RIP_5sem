import math
import sys


def sys_argv_input():
    result = list()
    for i in sys.argv[1:]:
        try:
            result.append(int(i))
            continue
        except ValueError:
            print("ValueError - некорректный ввод аргументов командной строки!")
            return None
    return {'a': result[0], 'b': result[1], 'c': result[2]}


def keyboard_input():
    print("Введите коэффициенты A, B, C квадратного уравнения c клавиатуры:")
    while True:
        try:
            a = int(input())
            b = int(input())
            c = int(input())
            break
        except ValueError:
            print("ValueError - некорректный ввод, попробуйте снова!")
    return {'a': a, 'b': b, 'c': c}


def calculation_equation(coef):
    a = coef['a']
    b = coef['b']
    c = coef['c']
    d = b * b - 4 * a * c
    # если A равно нулю, то уравнение линейное: Bx + C = 0
    if a == 0:
        # Bx = -C => x = -C / B
        if b != 0:
            print("a = 0 и b != 0, корень один: x1: {}".format(- c / b))
        print("a = 0 и b = 0 корней нет")
    elif d == 0:
        print("дискриминант равен 0, корень один: x1: {}".format(- b / (2 * a)))
    elif d > 0:
        r1 = (-b + math.sqrt(d)) / (2 * a)
        r2 = (-b - math.sqrt(d)) / (2 * a)
        print("дискриминант положительный, два корня: x1:{} x2:{}".format(r1, r2))
    elif d < 0:
        print("дискриминант отрицателен, действительных корней нет")


if __name__ == "__main__":
    print("Разработчик: Дюжев Степан Андреевич ИУ5Ц-73Б")

    if len(sys.argv) == 4:
        argv_coefficients = sys_argv_input()
        if argv_coefficients:
            calculation_equation(argv_coefficients)
        else:
            calculation_equation(keyboard_input())
    else:
        calculation_equation(keyboard_input())


