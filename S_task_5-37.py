"""Дано натуральное число N и последовательность из N элементов.
Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
"""

import random


def fill_str (num):
    num_seq = input ("Введите число от 0 до 9: ")
    if num == 1:
        return num_seq
    return fill_str (num - 1) + num_seq


num = random.randint(2, 5)
print(fill_str(num))