"""Даны два массива чисел. Требуется вывести те элементы первого массива 
(в том порядке, в каком они идут в первом массиве), которых нет во втором массиве"""

import random


def gen_list() -> list:
    return list(random.randint(-9, 99) for _ in range(random.randint(1, 50)))



def find_diff_lists(list1, list2: list) -> list:
    for i in range(len(list1)-1):
        for j in range(len(list2)-1):
            if list1[i] == list2[j]:
                list1.pop(i)
    return list1




list1 = gen_list()
list2 = gen_list()
print(f"Список 1 - {list1}")
print(f"Список 2 - {list2}")
print(f"Очищенный список - {find_diff_lists(list1, list2)}")
