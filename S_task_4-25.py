"""Напишите программу, которая принимает на вход строку, и отслеживает, 
сколько раз каждый символ уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
"""
my_input = "a a a b c a a d c d d"
my_list1 = my_input.split()
my_list2 = []
print (my_list1)
for i in range(len(my_list1)):
    if my_list1[i] not in my_list2:
        my_list2.append (my_list1[i])
    else:
        count_= 0
        while str(my_list1[i])+"_"+str(count_+1) in my_list2:
            count_ += 1
        my_list2.append (str(my_list1[i])+"_"+str(count_+1))
print(my_list2)
