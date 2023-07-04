"""Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на максимальные. 
Напишите программу, которая заменяет оценки Василия, но наоборот: 
все максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
"""

import random


def replace_int (source_list: list):
    print(source_list)
    replace_list = list()
    for i in range (len(source_list)):
        if source_list[i] == max(source_list):
            replace_list.append(min(source_list))
        else:
            replace_list.append(source_list[i])
            
    return (replace_list)


print(replace_int(list(random.randint(1, 5) for _ in range(random.randint(1, 33)))))