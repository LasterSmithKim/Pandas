import numpy as np
import pandas as pd

data = {
            'A': ['Dog', 'Dog', 'Dog', 'Goat', 'Goat', 'Goat'],
            'B': ['Brown', 'Brown', 'Black', 'Black', 'Brown', 'Brown'],
            'C': ['x', 'y', 'x', 'y', 'x', 'y'],
            'D': [1,3,2,5,4,1]
        }

df = pd.DataFrame(data)
print(df)

#  数据透视表的语法：  .pivot_table(data, values='', index=[''], columns=['']
#  values:需要汇总统计的数据点所在的列
#  index：表示按该列进行分组索引
#  columns：表示最后结果将按该列的数据进行分列
#  更多使用方法查询pandas官方文档

print(pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C']))
print(df.pivot_table(values='D', index=['A', 'B'], columns=['C']))