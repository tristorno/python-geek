"""
1. Изобразите отношение households к population с помощью точечного графика.
2. Визуализировать longitude по отношения к median_house_value, используя линейный график.
3. Представить гистограмму по housing_median_age.
4. Изобразить гистограмму по median_house_value с оттенком housing_median_age.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("california_housing_train.csv")
sns.scatterplot(data=df, x='longitude', y='median_house_value')
plt.show()