print("Введите первое число:")
first_num = int(input())
print("Введите второе число:")
second_num = int(input())

print("Результат сложения:", (first_num + second_num), '\n')

print("Введите первое число:")
first_num = int(input())
print("Введите второе число:")
second_num = int(input())

print("Результат вычитания:", (first_num - second_num), '\n')

print("Введите первое число:")
first_num = int(input())
print("Введите второе число:")
second_num = int(input())

print("Результат умножения:", (first_num * second_num), '\n')

print("Введите первое число:")
first_num = int(input())
print("Введите второе число:")
second_num = int(input())

try:
    result = first_num / second_num
except ZeroDivisionError:
    print("На ноль делить нельзя!!")
except ValueError:
    print("Вы ввели нечисловое значение!")
else:
    print("Результат деления:", result)
