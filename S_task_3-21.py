"""Напишите программу для печати всех уникальных значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, 
{" VIII":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}"""

my_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
print (my_list)
result = set()
for i in my_list:
    for (k,v) in i.items():
        result.add(v)
print(result)