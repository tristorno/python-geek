"""Задача No23.
Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)"""

import random

list = list()
number = random.randint (3, 101)
for i in range (number):
    list.append (random.randint(-50,100))
result = 0
for i in range (len(list)-1):
    if list[i] < list[i+1]:
        result = result + 1

print (f"Список: {list}")
print (f"\nОтвет - {result}")