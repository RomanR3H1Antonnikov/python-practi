def sum_even_numbers():
    counter = 0
    for i in range(2, 101, 2):
        counter += i
    return counter


def square_odds():
    return [n ** 2 for n in range(1, 11, 2)]


print(sum_even_numbers(), square_odds())
counter = 0
print("Введите число:")
try:
    while True:
        counter += 1
        if int(input()) >= 0:
            continue
        else:
            break
    print("Количество введённых чисел:", counter)
except ValueError:
    print("Вы ввели не число! Введите число!")