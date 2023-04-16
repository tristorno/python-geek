"""
На столе лежат n монеток. 
Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть.
"""

import random

heads = 0
tails = 0
i=0
number = random.randint(2,50)
coin = -1
for i in range(number):
    coin = random.randint(0,1)
    print(coin, end=" ")
    i += 1
    if coin == 0:
        tails += 1
    else:
        heads += 1

if heads < tails:
    print("\nНадо перевернуть {} монет.".format(heads))
else:
    print("\nНадо перевернуть {} монет.".format(tails))
