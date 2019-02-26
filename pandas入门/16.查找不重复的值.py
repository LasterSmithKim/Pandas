import numpy as np
import pandas as pd


df = pd.DataFrame({'col1': [1, 2, 3, 4],'col2': [444, 555, 666, 444],'col3': ['abc', 'def', 'ghi', 'xyz']})
print(df.head())
df1 = df['col2'].unique()
print(df1)

df2 = df['col2'].nunique()
print(df2)

df3 = df['col2'].value_counts()
print(df3)



