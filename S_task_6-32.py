"""Определить индексы элементов списка, значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)"""

import Generate_list

min_num = int(input("Input min number: "))
max_num = int(input("Input max number: "))
print(my_list := Generate_list.gen_list())

print(f"Индексы элементов в заданном диапазлне: {[i for i in range(len(my_list)-16) if min_num < my_list[i] < max_num]}")