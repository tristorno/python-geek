"""Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
Задание необходимо решать через рекурсию
"""

def fibo (num):
    fibo_res = 0
    if num == 0:
        return 0
    fibo_res = num + fibo(num - 1)
    return fibo_res


num = 7
print (fibo(num-1))