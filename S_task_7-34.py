"""Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, 
насколько легко он их придумывает, Вам стоит написать программу. 
Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
если во фразе несколько слов, то они разделяются дефисами. 
Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает 
в программу с клавиатуры. В ответе напишите “Парам пам-пам”, 
если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    

**Вывод:** Парам пам-пам
"""
import string

phrase = input("Введите две фразы через пробел: ")
phrase_list = str.split(str.lower(phrase))
phrase1 = phrase_list[0]
phrase2 = phrase_list[1]
vowels = ("аёуеыоэяию")
phr1_vow = 0
phr2_vow = 0
for char in phrase1:
    if char in vowels:
        phr1_vow += 1

for char in phrase2:
    if char in vowels:
        phr2_vow += 1


print("Парам пам-пам" if phr1_vow == phr2_vow else "Пам парам")