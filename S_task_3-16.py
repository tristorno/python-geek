"""Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N]"""
#вариант мой
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

#вариант препода
my_list_ = [random.randint(1,10) for _ in range (random.randint(3,20))]
print(my_list_)
num = int(input("\nКакое число ищем? "))
print(my_list_.count(num))
