import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.rand(5,4),columns=list('ABCD')).round(2)
print(df*100)


#Creating DataFrame from a dictionary of Series
df = {'Name': pd.Series(['Jon', 'Aaron', 'Todd'],index=['a', 'b', 'c']),
      'Age': pd.Series(['39', '34', '32', '33'],index=['a', 'b', 'c', 'd']),
      'Nationality': pd.Series(['US', 'CN', 'US'],index=['a', 'b', 'c']),
     }
print(pd.DataFrame(df))


#Creating DataFrame from a dictionary of list
data = {'name': ['George', 'Ann', 'Tino', 'Charles', 'Phil'],
        'age': [40, 24, 31, 21, 23],
        'year': [2012, 2012, 2013, 2014, 2014]
        }
my_df = pd.DataFrame(data, index= ['Lagos', 'Dubai', 'Mumbai', 'Accra', 'Yuma'])
print(my_df)
















