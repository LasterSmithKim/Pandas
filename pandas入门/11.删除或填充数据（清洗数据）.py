import numpy as np
import pandas as pd


dt = {'A': [1, np.nan, 3], 'B': [2, np.nan, np.nan], 'C': [4, 5, 6]}
dt = pd.DataFrame(dt)
print(dt)

#Let's drop the rows with null values
dt1 = dt.dropna()
print(dt1)
#默认删除行，axis=1 删除列   axis=0 删除行
dt1 = dt.dropna(axis=1)
print(dt1)

dt1 = dt.dropna(axis=0)
print(dt1)

dt2 = dt.fillna('20')
print(dt2)
