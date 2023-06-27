"""Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N]"""

import random
length = random.randint(3, 20)
my_list = []
count = 0
for i in range(length):
    my_list.append(random.randint(1,9))
print (my_list)

num = int(input("\nКакое число ищем? "))
for i in range(length):
    if my_list[i] == num:
        count += 1

print (count)
