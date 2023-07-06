"""Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
Задание необходимо решать через рекурсию
"""

def fibo (num):
    if num in [0, 1]:
        return 1
    return fibo(num-1) + fibo(num-2)


num = int(input("Введите число: "))
print (fibo(num))