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


def remove_book(title):
    if title in library:
        del library[title]
        print(f'Книга "{title}" успешно удалена из библиотеки')
    else:
        print("Такой книги нет в библиотеке!")


def issue_book(title):
    if title in library and library[title]['availability'] != False:
        library[title]['availability'] = False
        print(f"Книга {title} выдана!")
    elif library[title]['availability'] == False:
        print("Для аренды книги она должна быть в библиотеке.")
    else:
        print("Такой книги нет в библиотеке!")


def return_book(title):
    if title in library and library[title]['availability'] == False:
        library[title]['availability'] = True
        print(f"Книга {title} возвращена!")
    elif library[title]['availability'] != False:
        print("Для возврата книги сначала требуется её арендовать.")
    else:
        print("Такой книги нет в истории библиотеки!")


library = {
    "Братья Карамазовы": {
    "author": "Ф.М. Достоевский",
    "publishing_year": 1879,
    "availability": True
}}

book_list_view(library)
add_book(library, '1984', 'J. Oruell', '1988')
book_list_view(library)
add_book(library, '1984', 'J. Oruell', '1988')
book_list_view(library)
remove_book("Братья Карамазовы")
print(library)
return_book('1984')
print(library)
issue_book('1984')
issue_book('1984')