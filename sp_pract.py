def sum_lists(list_1, list_2):
    final_list = []
    if len(list_1) >= len(list_2):
        maximal_list = list_1
        minimal_list = list_2
    else:
        maximal_list = list_2
        minimal_list = list_1

    for i in range(len(maximal_list)):
        if i < len(minimal_list):
            final_list.append(maximal_list[i] + minimal_list[i])
        else:
            final_list.append(maximal_list[i])
    return final_list


list_1 = [1, 2, 3, 4, 5, 6, 7]
list_2 = [1, 2, 3, 4]
print(sum_lists(list_1, list_2))