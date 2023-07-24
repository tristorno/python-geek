"""
1. Прочесть с помощью pandas файл california_housing_test.csv/
2. Посмотреть сколько в нем строк и столбцов
3. Определить какой тип данных имеют столбцы
"""

import pandas

my_data = pandas.read_csv("california_housing_train.csv")
shape = my_data.shape
print(shape)
print(my_data.dtypes)