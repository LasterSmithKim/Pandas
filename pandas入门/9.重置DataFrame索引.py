import numpy as np
import pandas as pd

#默认新的index是  01234...
df = pd.DataFrame(np.random.randn(5,4),['a', 'b', 'c', 'd', 'e'],['W', 'X', 'Y', 'Z'])
df1 = df.reset_index()
print(df1)

df['ID'] = ['df1', 'df2', 'df3', 'df4', 'df5']
print(df)

df2 = df.set_index('ID')
print(df2)
