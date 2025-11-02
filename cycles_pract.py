try:
    num = int(input("Введите целое положительное число: "))
    if num > 0 and isinstance(num, int):
        while num != -1:
            print(num)
            num -= 1
    else:
        print("Вы ввели отрицательное число!")
except ValueError:
    print("Вы ввели не целое число!")