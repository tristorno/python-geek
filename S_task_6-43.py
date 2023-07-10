"""Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вывести эти пары в отдельных строках."""

import Generate_list


def find_pare_elem(list_num: list) -> int:
    count_pare = 0
    for i in range(len(list_num)-1):
        for j in range(i+1, len(list_num)-1):
            if list_num[i] == list_num [j]:
                print(f"{list_num[i]} <-> {list_num[j]}")
                count_pare += 1
    return count_pare



    return pare_list


print(my_list:= Generate_list.gen_list())
print("Найденные пары: ")
print(f"Всего найдено {find_pare_elem(my_list)} пар элементов.")