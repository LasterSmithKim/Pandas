import numpy as np
import pandas as pd


df = pd.DataFrame({'col1': [1, 2, 3, 4],'col2': [444, 555, 666, 444],'col3': ['abc', 'def', 'ghi', 'xyz']})

def square(x):
    return x*x

df1 = df['col1'].apply(square)
print(df1)



df2 = df['col3'].apply(len)
print(df2)
