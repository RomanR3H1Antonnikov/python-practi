def sum_lists(list_1, list_2):
    final_list = []
    maximal_list = max(list_1, list_2, key=len)
    minimal_list = min(list_1, list_2, key=len)

    for i in range(len(maximal_list)):
        if i < len(minimal_list):
            final_list.append(maximal_list[i] + minimal_list[i])
        else:
            final_list.append(maximal_list[i])
    return final_list


list_1 = [1, 200, 3, 4, 5, 6, 7]
list_2 = [1, 2, 3, 400000]
print(sum_lists(list_1, list_2))