import numpy as np
import pandas as pd


#读取CSV文件
df = pd.read_csv('example.csv')
print(df)

#写入CSV文件
data = {
            'A': ['Dog', 'Dog', 'Dog', 'Goat', 'Goat', 'Goat'],
            'B': ['Brown', 'Brown', 'Black', 'Black', 'Brown', 'Brown'],
            'C': ['x', 'y', 'x', 'y', 'x', 'y'],
            'D': [1,3,2,5,4,1]
        }
df1 = pd.DataFrame(data)
print(df1)
#Now we can save the df in a 'New_dataframe' which pandas auto-creates for us
#这里的 index=False 表示不将 索引列0~5 放入文件中
df1.to_csv('New_dataFrame.csv', index=False)

#读取Excel表格文件


