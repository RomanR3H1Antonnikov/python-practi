def book_list_view(library):
    found_books = False
    for book_title, details in library.items():
        if all(x != '' for x in details.values()):
            print(f"""Книга: {book_title} Информация о книге: {details} """)
            found_books = True
    if not found_books:
        print("В библиотеке нет книг.")


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