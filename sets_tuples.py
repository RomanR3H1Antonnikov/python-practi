list_1 = []
print("Вводите числа, заполняя список, введите -2, чтобы получить количество уникальных элементов в списке:")
try:
    while True:
        current_num = int(input())
        if current_num != -1:
            list_1.append(current_num)
        else:
            break
except ValueError:
    print("Вводите числовые значения!")
print(f"""Количество уникальных элементов в списке: {len(set(list_1))}""")