"""
//////////////////////////////////////////////////////////////////////////
Найдите сумму цифр трехзначного числа.////////////////////////////////////
//////////////////////////////////////////////////////////////////////////.
"""

print("Введите число от 100 до 999: ")
num = int(input())
if 99<num<1000:
    result = num%10
    num //= 10
    result = result + num%10 + num//10 
    print("Сумма цифр этого числа равна", result)

else:
    print("Введено некорректное число")