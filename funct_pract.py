def max_number(a, b):
    if a > b:
        return a
    return b


def empty_function():
    pass


def even_numbers(n):
    for x in range(0, n + 1, 2):
        yield x

def test_max_number():
    assert max_number(1, 4) == 4, "Ошибка, 4 больше чем 1!"
    assert max_number(-4, 3) == 3, "Ошибка, 3 больше чем -4!"
    assert max_number(2, 2) == 2, "Ошибка, числы должны быть различными!"
    print("Проверка успешно пройдена!")


print(max_number(4, 10))
print(empty_function())
for num in even_numbers(6):
    print(num)
test_max_number()