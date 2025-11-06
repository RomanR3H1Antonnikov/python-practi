def max_list(list_1, list_2):
    if len(list_1) >= len(list_2):
        return list_1
    else:
        return list_2


def min_list(list_1, list_2):
    if len(list_1) <= len(list_2):
        return list_1
    else:
        return list_2


list_1 = [1, 2, 3, 4, 5, 6, 7]
list_2 = [1, 2, 3, 4]
final_list = []
maximal_list, minimal_list = max_list(list_1, list_2), min_list(list_1, list_2)


for i in range(0, maximal_list):
    if i < len(minimal_list):
        final_list.append(maximal_list[i] + minimal_list[i])
    else:
        final_list.append(max_list(list_1, list_2)[i])
print(final_list)