from math import acos, factorial
from random import uniform

def help():
    print("Вы воспользовались командой 'help', чтобы узнать какие операторы доступны:")
    print("+, -, /, *, ^")
    print("'module' - находит модуль числа")
    print("'random' - рандомное число")
    print("'!' - факториал числа")
    print("'arccos' - арккосинус числа")

# Операции:
# Где один операнд: модуль, факториал и арккосинус.
# Где два операнда: +, -, /, *, возведение в степень(^), рандомное число(random).
print("Добро пожаловать в мини-калькулятор, в данном калькуляторе доступны такие операторы:")
print("+, -, /, *, ^")
print("'module' - находит модуль числа")
print("'random' - рандомное число")
print("'!' - факториал числа")
print("'arccos' - арккосинус числа")

state = 'y'

while state != 'n':
    operator = input("Выберите оператор и введите его: ")

    match operator:
        case "+":
            num1, num2 = map(float, input("Введите два числа через пробел: ").split())
            print(f"Результат: {num1 + num2}")
        case "-":
            num1, num2 = map(float, input("Введите два числа через пробел: ").split())
            print(f"Результат: {num1 - num2}")
        case "/":
            num1, num2 = map(float, input("Введите два числа через пробел: ").split())
            try:
                print(f"Результат: {num1 / num2}")
            except ZeroDivisionError:
                print(f"Ты не можешь делить {num1} на ноль!")
        case "*":
            num1, num2 = map(float, input("Введите два числа через пробел: ").split())
            print(f"Результат: {num1 * num2}")
        case "^":
            num1 = float(input("Введите основание степени: "))
            num2 = float(input("Введите степень: "))
            if (num1 != 0) and (num2 != 0):
                print(f"Результат: {num1 ** num2}")
            else:
                print(f"{num1} нельзя возводить в степень {num2}")
        case "module":
            num1 = float(input("Введите число: "))
            print(f"Результат: {abs(num1)}")
        case "random":
            num1 = float(input("Введите нижнюю границу: "))
            num2 = float(input("Введите верхнюю границу: "))
            print(f"Результат: {uniform(num1, num2)}")
        case "!":
            num1 = int(input("Введите число: "))
            if num1 >= 0:
                print(f"Результат: {factorial(num1)}")
            else:
                print(f"Факториал для данного ({num1}) числа не поддерживается.")
        case "arccos":
            num1 = float(input("Введите число: "))
            if abs(num1) <= 1:
                print(f"Результат: {acos(num1)}")
            else:
                print(f"Арккосинуса данного ({num1}) числа не существует.")
        case "help":
            help()
        case _:
            print("Ввели неподдерживаемый оператор!")
            print("Попробуйте заново.")
            print("Если вы забыли команды, то введите: 'help', если не надо любую другую.")

    state = input("Если хотите продолжить нажмите 'y', если закончить 'n': ")
