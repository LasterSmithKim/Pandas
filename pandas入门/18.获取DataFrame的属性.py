import numpy as np
import pandas as pd

#We can clearly see the column names in our DataFrame
df = pd.DataFrame({'col1': [1, 2, 3, 4],'col2': [444, 555, 666, 444],'col3': ['abc', 'def', 'ghi', 'xyz']})

print(df.columns)
print(df.index)


# 排序

df1 = df.sort_values('col2')
print(df1)

#找空值
df1 = df.isnull()
print(df1)


