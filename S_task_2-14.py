"""
Требуется вывести все целые степени двойки, не превосходящие числа N.
"""

number = int(input("Введите число: "))
i = 0
mult = 0
while mult < number:
    print (mult, end=" ")
    mult = 2 ** i
    i += 1