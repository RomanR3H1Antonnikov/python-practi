# def is_participation_approved(age, citizenship, is_disqualified):
#     if age < 18 or citizenship == "Нет" or is_disqualified == "Да":
#         return False
#     elif citizenship != "Да" or is_disqualified != "Нет":
#         print("Нужно ответить 'Да' или 'Нет'!!")
#         return False
#     return True
#
#
# age = int(input("Укажите ваш возраст: "))
# citizenship = input("Вы являетесь гражданином страны? Ответьте 'Да' или 'Нет': ")
# is_disqualified = input("Вы не дисквалифицированы? Ответьте 'Да' или 'Нет': ")
# if is_participation_approved(age, citizenship, is_disqualified):
#     print("Поздравляю, вам можно голосовать на выборах!")
# else:
#     print("К сожалению, вы не можете принимать участие в выборах")

num_slv = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}
print("Соответствующее слово:", num_slv[int(input('Введите число от 1 до 5: '))])