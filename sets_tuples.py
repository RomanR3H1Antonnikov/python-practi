def get_valid_input(inpt):
    while True:
        value = input(inpt).strip()
        if value:
            return value
        print("Название книги не может быть пустым!")


def print_menu(menu_data):
    print("Доступные функции:")
    for key in sorted(menu_data.keys()):
        text, _ = menu_data[key]
        print(f"{key}. {text}")
    print("Введите номер функции: (1 - 7)")


def book_list_view(library):
    if not library:
        print("В библиотеке нет книг.")
    else:
        print("Доступные книги:")
        for book_title in library:
            print(f"'{book_title}'")


def add_book_handler(library):
    print("Введите через запятую название книги, автора и год выпуска:")
    data = input().split(',')
    if len(data) == 3:
        title, author, year_str = data[0].strip(), data[1].strip(), data[2].strip()
        try:
            year = int(year_str)
            add_book(library, title, author, year)
        except ValueError:
            print("Год выпуска должен быть числом!")
    else:
        print("Ошибка формата")


def add_book(library, title, author, year):
    if title not in library:
        library[title] = {
            "author": author,
            "publishing_year": year,
            "availability": None
        }
        print(f"""Книга "{title}" успешно добавлена!""")
    else:
        print("Книга с таким названием уже существует. Хотите обновить информацию о ней? (Да/Нет)")
        if input().lower() == "да":
            library[title] = {
                "author": author,
                "publishing_year": year,
                "availability": None
            }
            print(f"""Информация о книге {title} успешно обновлена!""")
        else:
            print("Вы не ответили 'Да', операция отменена")


def remove_book(library, title):
    if title in library:
        del library[title]
        print(f'Книга "{title}" успешно удалена из библиотеки')
    else:
        print("Такой книги нет в библиотеке!")


def issue_book(library, title):
    if title in library and library[title]['availability'] is not False:
        library[title]['availability'] = False
        print(f"Книга {title} выдана!")
    elif title in library and library[title]['availability'] is False:
        print("Книга уже выдана!")
    else:
        print("Такой книги нет в библиотеке!")


def return_book(library, title):
    if title in library and library[title]['availability'] is False:
        library[title]['availability'] = True
        print(f"Книга {title} возвращена!")
    elif title in library and library[title]['availability'] is not False:
        print("Для возврата книги сначала требуется её арендовать.")
    else:
        print("Такой книги нет в истории библиотеки!")


def find_book(library, title):
    if title in library:
        condition = "Книга в библиотеке, но ее статус не определен"
        if library[title]["availability"] is False:
            condition = "Книга выдана"
        if library[title]["availability"] is True:
            condition = "Книга доступна"
        print(f"Книга найдена! Название: '{title}'\nАвтор: {library[title]["author"]}, год выпуска: {library[title]["publishing_year"]}, статус: {condition}")
    else:
        print(f"Книга {title} не найдена")


def start_menu(library):
    text_to_write = "Введите название книги:"
    menu_data = {
        1: ("Список книг в библиотеке", lambda: book_list_view(library)),
        2: ("Добавить книгу в библиотеку", lambda: add_book_handler(library)),
        3: ("Удалить книгу из библиотеки", lambda: remove_book(library, get_valid_input(text_to_write))),
        4: ("Арендовать книгу", lambda: issue_book(library, get_valid_input(text_to_write))),
        5: ("Вернуть книгу", lambda: return_book(library, get_valid_input(text_to_write))),
        6: ("Поиск книг", lambda: find_book(library, get_valid_input(text_to_write))),
        7: ("Закрыть меню", None)
    }
    while True:
        try:
            print_menu(menu_data)
            command = int(input())

            if command == 7:
                print("Работа завершена, хорошего дня!")
                break
            elif command in menu_data:
                _, action = menu_data[command]
                if action:
                    action()
            else:
                print("Неверная команда!")

        except ValueError:
            print("Команда не введена!")


library = {
    "Братья Карамазовы": {
    "author": "Ф.М. Достоевский",
    "publishing_year": 1879,
    "availability": True
}}


start_menu(library)