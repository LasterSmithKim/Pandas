import numpy as np
import pandas as pd

data = {'name': ['George', 'Ann', 'Tino', 'Charles', 'Phil'],
        'age': [40, 24, 31, 21, 23],
        'year': [2012, 2012, 2013, 2014, 2014]
        }
my_df = pd.DataFrame(data, index= ['Lagos', 'Dubai', 'Mumbai', 'Accra', 'Yuma'])
print(my_df['name'])

print(type(my_df['name']))


#获取多个列，注意使用双 中括号
print(my_df[['name', 'year']])



