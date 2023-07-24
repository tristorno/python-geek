"""Работать с файлом california_housing_train.csv. 
Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).
"""

import pandas as pd

df = pd.read_csv("california_housing_train.csv")