"""
Создать календарь наблюдаемых температур воздуха за n дней.
Вычислить самую длинную последовательность положительных температур.
"""

import random
calendar = 20 #int(input("Введите число рассматриваемых дней: "))
today = -100
i=0
seq_of_warm_days = 0
max_sequence = seq_of_warm_days
while i < calendar:
    today = random.randint(-10, 10)
    print(today, end = " ")
    i += 1
    if today > 0:
        seq_of_warm_days += 1
    elif seq_of_warm_days > max_sequence:
        max_sequence = seq_of_warm_days
        #print (f"Оттепель равна {seq_of_warm_days} дням")
        seq_of_warm_days = 0
    else:
        seq_of_warm_days = 0
if seq_of_warm_days > max_sequence:
        max_sequence = seq_of_warm_days
        
print (f"\nИТОГО \nМаксимальная оттепель равна {max_sequence} дням")