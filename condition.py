def is_participation_approved(age, citizenship, is_disqualified):
    if age < 18:
        return False
    if citizenship == "Нет":
        return False
    elif citizenship != "Да":
        print("Нужно ответить 'Да' или 'Нет'!!")
        return False
    if is_disqualified == "Да":
        return False
    return True


if is_participation_approved(int(input("Укажите ваш возраст: ")), input("Вы являетесь гражданином страны? Ответьте 'Да' или 'Нет': "),
                             input("Вы не дисквалифицированы? Ответьте 'Да' или 'Нет': ")):
    print("Поздравляю, вам можно голосовать на выборах!")
else:
    print("К сожалению, вы не можете принимать участие в выборах")