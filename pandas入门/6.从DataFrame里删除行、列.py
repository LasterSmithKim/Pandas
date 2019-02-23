import numpy as np
import pandas as pd

df = dict(Name=pd.Series(['Jon', 'Aaron', 'Todd'], index=['a', 'b', 'c']),
          Age=pd.Series(['39', '34', '32', '33'], index=['a', 'b', 'c', 'd']),
          Nationality=pd.Series(['US', 'CN', 'US'], index=['a', 'b', 'c']))
df['year'] = pd.Series(['2016', '2015', '2018', '2015'], ['a', 'b', 'c', 'd'])
df['Birth_year'] = df['year'] + df['Age']

df1 = pd.DataFrame(df)
print(df1)


#注意：除非用户明确指定，否则调用.drop()的时候，Pandas不会真的永久删除这条数据 行 列，
df2 = df1.drop('Birth_year', axis=1)
print(df2)

df2 = df1.drop('d', axis=0)
print(df2)

