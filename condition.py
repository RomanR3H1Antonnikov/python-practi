num_slv = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}
try:
    inc_num = int(input('Введите число от 1 до 5: '))
    if inc_num not in num_slv:
        print("Вы ввели неверное число!")
    else:
        print("Соответствующее слово:", num_slv[inc_num])
except ValueError:
    print("Вы ввели не число!")