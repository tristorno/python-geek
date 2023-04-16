"""
Написать программу, которая проверяет счастливость билета.
Счастливым называют такой билет с шестизначным номером, где сумма
первых трех цифр равна сумме последних трех. Т.е. билет с номером
385916 – счастливый, т.к. 3+8+5=9+1+6.
"""

import random
number = random.randint(100000,999999)
print ("Номер билетика - ",number)
num_left = (number//1000)%10 + (number//10000)%10 + (number//100000)%10
num_right = number%10 + (number//10)%10 + (number//100)%10 
if num_left==num_right:
    print(f"{num_left} = {num_right} - билет счастливый!!!")
else:
    print(f"{num_left} не равно {num_right} - не повезло.")