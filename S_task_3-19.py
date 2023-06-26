"""Дана последовательность из N целых чисел и положительное число K. 
Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]"""

import random

my_list = list ([1, 2, 3, 4, 5])
print (my_list)
print ("Insert number: ")
k = int (input())
if k < 0:
    k = k * -1
k = k % len(my_list)
new_list = my_list[-k+1:] + my_list[:-k+1]
print (new_list)