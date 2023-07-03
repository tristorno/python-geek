""" В фермерском хозяйстве в Карелии выращивают чернику. 
Она растёт на круглой грядке, причём кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора 
на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать 
за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
"""
import random

bush_list = [random.randint(0,10) for _ in range(random.randint(3,10))]
print (bush_list)

berry_dict = {}
for i in range (len(bush_list)-2):
    berry_dict[i] = bush_list[i]+bush_list[i+1]+bush_list[i+2]
berry_dict[len(bush_list)-2] = bush_list[-2]+bush_list[-1]+bush_list[0]
berry_dict[len(bush_list)-1] = bush_list[-1]+bush_list[0]+bush_list[1]

max_berry_value = 0
max_berry_key = -1
for (k, v) in berry_dict.items():
    if max_berry_value < v:
        max_berry_value = v
        max_berry_key = k

max_bush_num = max_berry_key+1 if max_berry_key < (len(bush_list)-1) else 0

print(f"Номер куста - {max_bush_num+1}, \nКоличество ягод - {max_berry_value}")
