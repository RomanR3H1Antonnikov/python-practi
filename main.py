try:
    print("Введите первое число:")
    first_num = int(input())
    print("Введите второе число:")
    second_num = int(input())
    result = first_num + second_num
except ValueError:
    print("Вы ввели нечисловое значение!")
else:
    print("Результат сложения:", result, '\n')

try:
    print("Введите первое число:")
    first_num = int(input())
    print("Введите второе число:")
    second_num = int(input())
    result = first_num - second_num
except ValueError:
    print("Вы ввели нечисловое значение!")
else:
    print("Результат вычитания:", result, '\n')

try:
    print("Введите первое число:")
    first_num = int(input())
    print("Введите второе число:")
    second_num = int(input())
    result = first_num * second_num
except ValueError:
    print("Вы ввели нечисловое значение!")
else:
    print("Результат умножения:", result, '\n')

try:
    print("Введите первое число:")
    first_num = int(input())
    print("Введите второе число:")
    second_num = int(input())
    result = first_num / second_num
except ZeroDivisionError:
    print("На ноль делить нельзя!!")
except ValueError:
    print("Вы ввели нечисловое значение!")
else:
    print("Результат деления:", result)
