library = {"book_name": {"author": "", "publishing_year": "", "availability": ""}}

def book_list_view(library):
    if library["book_name"]["author"] and library["book_name"]["publishing_year"] and library["book_name"]["availability"]:
        print(library["book_name"])
    else:
        print("В библиотеке нет книг.")


book_list_view(library)