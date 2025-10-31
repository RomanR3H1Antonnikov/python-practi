# double_quote_str = "\"Hello, World\""
# single_quote_str = "\'Hello, World\'"
# path_str = "C:\\path\\example"
# new_string_string = "First string\nsecond string"
#
# multistring_string = """'Лень' \t - двигатель прогресса \n однако это ещё и признак, что человека сейчас всё устраивает"""
#
# print(double_quote_str, single_quote_str, path_str, new_string_string, multistring_string, sep='\n')

# name = "Роман"
# hobby = 'Бокс'
# favourite_film = """'Зелёная книга' — американская биографическая комедийная драма режиссёра Питера Фаррелли,
#  вышедшая на экраны в 2018 году. Картина рассказывает реальную историю путешествия по югу США
#   знаменитого джазового пианиста Дона Ширли и обычного водителя Тони Валлелонги, между которыми
#    со временем возникает дружба. Главные роли исполнили Вигго Мортенсен, Махершала Али и Линда Карделлини."""
# print(name, hobby, favourite_film, sep='\n')

# word = "Programming"
# print(word[0], word[-1])
# print(word[:5])
# print(word[3:])

# name = "Роман"
# surname = "Антонников"
# print(name + " " + surname)
# greeting = "Hello!"
# print(greeting * 3)

# age = 18
# city = "Moscow"
# format_string = "My age is {}, I live in {}".format(age, city)
# ftype_string = f"My age is {age}, I live in {city}"
# print(format_string, ftype_string)

# spaceline_string = "                something           "
# print(spaceline_string.strip())
# facts = "cats says hello"
# print(facts.replace("hello", "meow"))
# base = "Python is great"
# print(base.split())
# str_sp = ['h', 'e', 'l', 'l', 'o']
# print("".join(str_sp))


result = True
result = False if int(input("Введите ваш возраст, только число")) < 18 else True
result = False if input("Вы являетесь гражданином страны?").lower().strip() != "да" else True
result = False if input("Вы уголовно наказуемый(ая)?").lower().strip() != "нет" else True
print("Поздравляю, вам можно голосовать на выборах!") if result == True else print("К сожалению,"
                                                                           " вы не можете принимать участие в выборах")