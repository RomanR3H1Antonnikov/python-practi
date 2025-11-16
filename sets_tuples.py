def book_list_view(library):
    if not library:
        print("В библиотеке нет книг.")
    else:
        for book_title in library:
            print(f"Доступные книги:\n{book_title}")


# def add_book(title, author, year):
#     if title not in library:
#         library[title] = {
#             "author": author,
#             "publishing_year": year,
#             "availability": None
#         }
#         print(f"""Книга "{title}" успешно добавлена!""")
#     else:
#         print("Книга с таким названием уже существует. Хотите обновить информацию о ней?")
#         if input().lower() == "да":
#             library[title] = {
#                 "author": author,
#                 "publishing_year": year,
#                 "availability": None
#             }
#             print(f"""Информация о книге {title} успешно обновлена!""")
#         else:
#             pass


library = {
    "Братья Карамазовы": {
    "author": "Ф.М. Достоевский",
    "publishing_year": 1879,
    "availability": True
}}
book_list_view(library)
# add_book('1984', 'J. Oruell', '1988')
# book_list_view(library)
# add_book('1984', 'J. Oruell', '1988')
# book_list_view(library)