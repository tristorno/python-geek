"""
Написать функцию transformation, чтобы было ok.

Ввод:
values = [1, 23, 42, 'asdfg']
transformed_values = list(map(trasformation, values))
if values == transformed_values:
print('ok')
else:
print('fail')

Вывод:
ok

"""
trasformation = lambda x : x

values = [1, 23, 42, 'asdfg']
transformed_values = list(map(trasformation, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')