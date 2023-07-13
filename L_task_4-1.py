"""Из списка выдернуть четные числа и сделать вывод: [(число, квадр_числа)]"""

import Generate_list

print(my_list := Generate_list.gen_list())

def find_sqr_even(my_list: list) -> list:
    new_list = list()
    for i in my_list:
        if i % 2 == 0:
            new_list.append((i, i*i))
    return new_list
        
print(find_sqr_even(my_list))

