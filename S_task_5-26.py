"""Напишите программу, которая на вход принимает два числа A и B 
и возводит число А в целую степень B с помощью рекурсии."""

def count_num_power (num, num_power: int) -> int:
    """Функция возведения числа в степень"""
    
    if num_power == 1:
        return num
    return num * count_num_power (num, num_power-1)


num = int(input("Введите число: "))
power = int(input("Введите степень: "))
print(f"{num} в степени {power} равно {count_num_power(num, power)}")
