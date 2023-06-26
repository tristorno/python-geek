#Дан список чисел. Определите, сколько в нем встречается различных чисел.


import random

list_num = list()
number = random.randint (2, 500)
for i in range (number):
    list_num.append(random.randint(-50,50))
print (f"\nНачальный список: {list_num}")
for i in range (len(list_num)-2):
    j = i + 1
    while j < len(list_num):
        if list_num[i] == list_num[j]:
            list_num.pop(j)
        else:
            j+=1

print (f"\nУникальный список: {list_num}")
print (f"\nКоличество уникальных значений равно {len(list_num)}")

