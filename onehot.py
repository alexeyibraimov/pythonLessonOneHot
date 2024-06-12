import pandas as pd
import random

# Исходные данные
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Решение
one_hot = pd.DataFrame(0, index=data.index, columns=['human', 'robot'])

for i in data.index:
    one_hot.at[i, data.loc[i, 'whoAmI']] = 1

result = pd.concat([data, one_hot], axis=1)

print(result.head())