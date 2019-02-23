import numpy as np
import pandas as pd



df = {'Name': pd.Series(['Jon', 'Aaron', 'Todd'],index=['a', 'b', 'c']),
      'Age': pd.Series(['39', '34', '32', '33'],index=['a', 'b', 'c', 'd']),
      'Nationality': pd.Series(['US', 'CN', 'US'],index=['a', 'b', 'c'])
     }
print(pd.DataFrame(df))

#重新定义一个Series，把它放入到表中
#Creating a new column from a Series
df['year'] = pd.Series(['2016', '2015', '2018', '2015'], ['a', 'b', 'c', 'd'])
print(pd.DataFrame(df))


#从现有列，创建新列
df['Birth_year'] = df['year'] + df['Age']
print(pd.DataFrame(df))