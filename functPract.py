from test1 import result


def max_number(a, b):
    if a > b:
        return a
    elif a == b:
        print("Числа должны быть различными!")
        return None
    else:
        return b


def empty_function():
    pass


def even_numbers(n):
    if n % 2 == 0:
        yield n


def test_max_number():
    assert max_number(1, 4) == 4, "Ошибка, 4 больше чем 1!"
    assert max_number(-4, 3) == 3, "Ошибка, 3 больше чем -4!"
    assert max_number(2, 2) is None, "Ошибка, числы должны быть различными!"
    print("Проверка успешно пройдена!")


max_number(4, 7)
empty_function()
even_numbers(6)
test_max_number()