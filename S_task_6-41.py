"""Дан массив, состоящий из целых чисел. 
Напишите программу, которая в данном массиве определит количество элементов, 
у которых есть два соседних и, при этом, оба соседних элемента меньше данного"""


import Generate_list


def find_elem (list_num: list) -> int:
    count_num = 0
    for i in range (1, len(list_num)-1):
            if list_num[i-1] < list_num[i] > list_num[i+1]:
                count_num += 1

    return count_num

print(my_list := Generate_list.gen_list())
print(f"Найдено {find_elem(my_list)} элементов")
