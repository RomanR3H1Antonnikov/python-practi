def get_cleaned_word(word):
    return word.strip(',./?;:)(!@#$%^&*"\'')


def count_vowels(word):
    count = 0
    for char in word:
        if char in 'ёуеыаоэяию':
            count += 1
    return count


def process_text(text):
    text = text.strip().lower()
    longest_word = ''
    word_counter = 0
    vowel_counter = 0
    word_count_dict = {}

    for word in text.split():
        cleaned_word = get_cleaned_word(word)

        if not cleaned_word:
            continue

        word_counter += 1

        if len(cleaned_word) > len(longest_word):
            longest_word = cleaned_word

        vowel_counter += count_vowels(cleaned_word)

        if cleaned_word in word_count_dict:
            word_count_dict[cleaned_word] += 1
        else:
            word_count_dict[cleaned_word] = 1

    return word_count_dict, word_counter, longest_word, vowel_counter


text = input("Введите или пришлите текст: ")
word_count_dict, word_counter, longest_word, vowel_counter = process_text(text)

print("Вот слова и количество раз, которое каждое слово встречается в тексте: ")
for word, count in word_count_dict.items():
    print(f'{word}: {count}')
print("Количество слов в тексте:", word_counter)
print("Самое длинное слово в тексте:", longest_word)
print("Количество гласных букв:", vowel_counter)