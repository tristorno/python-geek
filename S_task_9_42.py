"""
Узнать какая максимальная households в зоне минимального значения population.
"""

import pandas as pd

df = pd.read_csv("california_housing_train.csv")

print(df.loc[(df.population.min()) , ["households"]].max())