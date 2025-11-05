def count_vowels(x):
    counter = 0
    for char in x:
        if char in 'ёуеыаоэяию':
            counter += 1
    return counter


def process_text(text):
    text = text.strip().lower()
    longest_word = ''
    word_counter = 0
    vowel_counter = 0
    word_count_dict = {}

    for word in text.split():
        word = word.strip(',./?;:)(!@#$%^&*"\'')
        word_counter += 1
        if len(word) > len(longest_word):
            longest_word = word
        vowel_counter += count_vowels(word)
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
    return word_count_dict, word_counter, longest_word, vowel_counter


text = input("Введите или пришлите текст: ")
word_count_dict, word_counter, longest_word, vowel_counter = process_text(text)
print("Вот слова и количество раз, которое каждое слово встречается в тексте: ")
for word, count in word_count_dict.items():
    print(f'{word}: {count}')
print("Количество слов в тексте:", word_counter)
print("Самое длинное слово в тексте:", longest_word)
print("Количество гласных букв:", vowel_counter)