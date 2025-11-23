def book_list_view(library):
    if not library:
        print("В библиотеке нет книг.")
    else:
        print("Доступные книги:")
        for book_title in library:
            print(f"'{book_title}'")


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
    while True:
        try:
            print(f'''Доступные функции:\n1. Список книг в библиотеке\n2. Добавить книгу в библиотеку\n3. Удалить книгу из библиотеки\n4. Арендовать книгу\n5. Вернуть книгу\n6. Поиск книг\n7. Закрыть меню''')
            print("Введите номер функции: (1 - 7)")
            command = int(input())
            if command == 1:
                book_list_view(library)
            elif command == 2:
                print("Введите через запятую название книги, автора и год выпуска:")
                data = input().split(',')
                if len(data) == 3:
                    title, author, year = data[0].strip(), data[1].strip(), data[2].strip()
                    try:
                        year = int(data[2].strip())
                        add_book(library, title, author, year)
                    except ValueError:
                        print("Год выпуска должен быть числом!")
                else:
                    print("Ошибка: введите данные в формате 'Название, Автор, Год'")
            elif command == 3:
                print("Введите название книги, которую хотите удалить:")
                title = input().strip()
                if not title:
                    print("Название книги не может быть пустым!")
                else:
                    remove_book(library, title)
            elif command == 4:
                print("Введите название книги, которую хотите арендовать:")
                title = input().strip()
                if not title:
                    print("Название книги не может быть пустым!")
                else:
                    issue_book(library, title)
            elif command == 5:
                print("Введите название книги, которую хотите вернуть в библиотеку:")
                title = input().strip()
                if not title:
                    print("Название книги не может быть пустым!")
                else:
                    return_book(library, title)
            elif command == 6:
                print("Введите название книги:")
                title = input().strip()
                if not title:
                    print("Название книги не может быть пустым!")
                else:
                    find_book(library, title)
            elif command == 7:
                print("Работа завершена, хорошего дня!")
                break
            else:
                print("Вы ввели не число от 1 до 7!")
        except ValueError:
            print("Команда не введена!")


library = {
    "Братья Карамазовы": {
    "author": "Ф.М. Достоевский",
    "publishing_year": 1879,
    "availability": True
}}


start_menu(library)