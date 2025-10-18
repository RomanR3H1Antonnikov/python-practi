try:
    print("Введите первое число:")
    first_num = int(input())
    print("Введите второе число:")
    second_num = int(input())
    result = first_num + second_num
    print("Результат сложения:", result, '\n')

    print("Введите первое число:")
    first_num = int(input())
    print("Введите второе число:")
    second_num = int(input())
    result = first_num - second_num
    print("Результат вычитания:", result, '\n')

    print("Введите первое число:")
    first_num = int(input())
    print("Введите второе число:")
    second_num = int(input())
    result = first_num * second_num
    print("Результат умножения:", result, '\n')

    print("Введите первое число:")
    first_num = int(input())
    print("Введите второе число:")
    second_num = int(input())
    try:
        result = first_num / second_num
        print("Результат деления:", result)
    except ZeroDivisionError:
        print("На ноль делить нельзя!!")
except ValueError:
    print("Вы ввели нечисловое значение!")