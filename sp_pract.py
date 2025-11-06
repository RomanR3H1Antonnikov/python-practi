# Вариант 1 - изменение значений и первого, и последнего элемента
sp_example = ["one", "two", "three", "four", "five"]
print(sp_example)
sp_example[0], sp_example[4] = "new_one", "new_five"
print(sp_example)

# Вариант 2 - меняем местами с помощью множественного присваивания
spsp = ["one", "two", "three", "four", "five"]
print(spsp)
spsp[0], spsp[4] = spsp[4], spsp[0]
print(spsp)