password = 'test-password123'
while True:
    if input("Введите пароль: ") != password:
        print("Неверный пароль, попробуйте ещё раз!")
        pass
    else:
        print("Пароль верный. Добро пожаловать!")
        break
