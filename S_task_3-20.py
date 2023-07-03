""" В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко; 
D, G – 2 очка; 
B, C, M, P – 3 очка; 
F, H, V, W, Y – 4 очка; 
K – 5 очков; 
J, X – 8 очков; 
Q, Z – 10 очков. 
А русские буквы оцениваются так: 
А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
Д, К, Л, М, П, У – 2 очка; 
Б, Г, Ё, Ь, Я – 3 очка; 
Й, Ы – 4 очка; 
Ж, З, Х, Ц, Ч – 5 очков; 
Ш, Э, Ю – 8 очков; 
Ф, Щ, Ъ – 10 очков. 
Напишите программу, которая вычисляет стоимость введенного пользователем слова."""

#Мой вариант
eng_1 = ('A', "E", "I", "O", "L", "N", "S", "T", "R")
eng_3 = ("B", "C", "M", "P")
eng_4 = ("F", "H", "V", "W", "Y")
eng_5 = ("K")
eng_8 = ("J", "X")
eng_10 = ("Q", "Z")
rus_1 = ("А", "В", "Е", "И", "Н", "О", "Р", "С", "Т")
rus_2 = ("Д", "К", "Л", "М", "П", "У")
rus_3 = ("Б", "Г", "Ё", "Ь", "Я")
rus_4 = ("Й", "Ы")
rus_5 = ("Ж", "З", "Х", "Ц", "Ч")
rus_8 = ("Ш", "Э", "Ю")
rus_10 = ("Ф", "Щ", "Ъ")
word = str.upper(input ("Введите слово: "))
print (word)
word_list = list(word)
print (word_list)
count = 0
for i in range (len(word_list)):
    if word_list[i] in eng_1:
        count += 1
print (count)

for i in range (len(word_list)):
    if word_list[i] in eng_3:
        count += 3
print (count)

for i in range (len(word_list)):
    if word_list[i] in eng_4:
        count += 4
print (count)

for i in range (len(word_list)):
    if word_list[i] in eng_5:
        count += 5
print (count)

for i in range (len(word_list)):
    if word_list[i] in eng_8:
        count += 8
print (count)

for i in range (len(word_list)):
    if word_list[i] in eng_10:
        count += 10
print (count)

for i in range (len(word_list)):
    if word_list[i] in rus_1:
        count += 1
print (count)

for i in range (len(word_list)):
    if word_list[i] in rus_2:
        count += 2
print (count)

for i in range (len(word_list)):
    if word_list[i] in rus_3:
        count += 3
print (count)

for i in range (len(word_list)):
    if word_list[i] in rus_4:
        count += 4
print (count)

for i in range (len(word_list)):
    if word_list[i] in rus_5:
        count += 5
print (count)

for i in range (len(word_list)):
    if word_list[i] in rus_8:
        count += 8
print (count)

for i in range (len(word_list)):
    if word_list[i] in rus_10:
        count += 10
print (f"ИТОГО: {count}")

#Вариант препода

points = {"AEIOULNSTRAEIOULNSTRАВЕИНОРСТ": 1,
          "DGДКЛМПУ": 2,
          "BCMPБГЁЬЯ": 3,
          "FHVWYЙЫ": 4,
          "KЖЗХЦЧ": 5,
          "JXШЭЮ": 8,
          "QZФЩЪ": 10}

word_ = input ("Введите слово: ")
score = 0

for letter in word_.upper():
    for letters in points:
        if letter in letters:
            score += points.get(letters)

print(score)