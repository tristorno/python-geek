"""
Петя, Катя и Сережа делают из бумаги журавликов. 
Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, 
что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
"""

print("Введите общее кол-во журавликов (кратно 6): ")
S = int(input())
if S<4 or S%6!=0:
    print("Введено некорректное значение!!!")
else:
    print(f"Катя сделала {int(S/3*2)} журавликов")
    print(f"Петя и Сережа сделали по {int(S/6)} журавликов, лодыри.")