import numpy as np
import pandas as pd


df = dict(Name=pd.Series(['Jon', 'Aaron', 'Todd'], index=['a', 'b', 'c']),
          Age=pd.Series(['39', '34', '32', '33'], index=['a', 'b', 'c', 'd']),
          Nationality=pd.Series(['US', 'CN', 'US'], index=['a', 'b', 'c']))
df['Year'] = pd.Series(['2016', '2015', '2018', '2015'], ['a', 'b', 'c', 'd'])
df['Birth_year'] = df['Year'] + df['Age']
df1 = pd.DataFrame(df)

print(df1.loc['a'])
print(df1.iloc[0])
print(df1.iloc[[0,1]])


#指定具体的行列范围，并生产一个子数据表，如提取 c 行中的 Name
print(df1.loc['b', 'Name'])
print(df1.loc[['b', 'c'],['Name', 'Year']])