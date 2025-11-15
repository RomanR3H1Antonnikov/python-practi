def book_list_view(library):
    if all(library["book_name"].values()):
        print(library["book_name"])
    else:
        print("В библиотеке нет книг.")


# def add_book(title, author, year):
#     if title not in library:
#         library["new_book_name"] = {
#             "author": author,
#             "publishing_year": year,
#             "availability": None
#         }
#         print(f"""Книга "{title}" успешно добавлена!""")
#     else:
#         print("Книга с таким названием уже существует. Хотите обновить информацию о ней?")
#         if input().lower() == "да":
#             library["new_book_name"] = {
#                 "author": author,
#                 "publishing_year": year,
#                 "availability": None
#             }
#             print(f"""Информация о книге {title} успешно обновлена!""")
#         else:
#             pass


library = {"book_name": {"author": "", "publishing_year": "", "availability": ""}}
# book_list_view(library)
# add_book('1984', 'J. Oruell', '1988')
# book_list_view(library)