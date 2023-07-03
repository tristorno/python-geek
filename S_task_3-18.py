"""Требуется найти в списке самый близкий по величине элемент к заданному числу X"""

import random
my_list = [random.randint(-9,100) for i in range(random.randint(3,30))]
print(my_list)

#вариант 1
num = int (input ("Введите искомое число: "))
res = -10
min_dif = 100
for i in range (len(my_list)):
    if (my_list[i] - num)**2 < min_dif**2:
        res = my_list[i]
        min_dif = my_list [i] - num
print (res)

