# password = 'test-password123'
# while True:
#     if input("Введите пароль: ") != password:
#         print("Неверный пароль, попробуйте ещё раз!")
#         pass
#     else:
#         print("Пароль верный. Добро пожаловать!")
#         break


text = input("Введите или пришлите текст: ").strip().lower()
longest_word = ''
word_counter = 0
vowel_counter = 0
slvr_words = {}
for word in text.split():
    word = word.strip(',./?;:)(!@#$%^&*"\'')
    word_counter += 1
    if len(word) > len(longest_word):
        longest_word = word
    for char in word:
        if char in 'ёуеыаоэяию':
            vowel_counter += 1
        elif char in ',./?;:)(!@#$%^&*':
            continue
    if word in slvr_words:
        slvr_words[word] += 1
    else:
        slvr_words[word] = 1
print("Вот слова и количество раз, которое каждое слово встречается в тексте: ")
for word in slvr_words:
    print(f'{word}: {slvr_words[word]}')
print("Количество слов в тексте:", word_counter)
print("Самое длинное слово в тексте:", longest_word)
print("Количество гласных букв:", vowel_counter)