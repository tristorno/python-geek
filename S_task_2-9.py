"""
Найти факториал введенного целого положительного числа через while
"""

i = 1
factorial = 1
num = int(input("Введите целое положительное число: "))
if (num<1):
    print("Ошибка ввода!")
else:
    while (i <= num):
        factorial = factorial * i
        i = i+1
print(factorial)