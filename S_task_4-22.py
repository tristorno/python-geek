""" Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах."""

import random

list_1 = list(random.randint(-99,100) for i in range(random.randint(3, 100)))
print (f"Первый список - {list_1}")
list_2 = list(random.randint(-99,100) for i in range(random.randint(3, 100)))
print (f"Второй список - {list_2}")
print (f"Общий список = {set.intersection(set(list_1), set(list_2))}")