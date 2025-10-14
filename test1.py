print("Введите два числа:")
a, b = int(input()), int(input())

try:
    result = a / b
except ValueError:
    print("Вы ввели нечисловое значение!")
except ZeroDivisionError:
    print("Делить на ноль нельзя!")
else:
    print(result)
finally:
    print("Завершение работы программы")