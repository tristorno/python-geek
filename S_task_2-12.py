"""
Петя задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.
"""

sum = int(input("Введите сумму двух чисел: "))
multiple = int(input("Введите произведение двух чисел: "))
first_num = 1
second_num = 1
while first_num <= 1000:
    while second_num <= 1000:
        if (first_num + second_num == sum) and (first_num * second_num == multiple):
            print("Загаданы {} и {}".format(first_num, second_num))
            exit (0)
        else:
            second_num += 1
    first_num += 1
    second_num = 0
print ("Обман!")

