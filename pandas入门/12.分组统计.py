import numpy as np
import pandas as pd

#First ,we create a DataFrame from a Dict
d = {'Company': ['GOOGLE', 'GOOGLE', 'ORACLE', 'ORACLE', 'TWITTER', 'TWITTER'],
     'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
     'Sales': [200, 120, 340, 124, 243, 350]}

dt = pd.DataFrame(d)
print(dt)

#Then Call the .groupby() method along with the aggregate .mean() method

dt1 = dt.groupby('Company').mean()
print(dt1)
#   .count() 可以统计元素出现的次数

# .describe() 描述数据统计指标 ：计数 平均数 标准差 最小值 25% 50% 75% 位置的值、 最大值 .describe().transpose()为竖版显示
# dt1 = dt.groupby('Company').describe().transpose()['GOOGLE'] 竖版显示 单独的数据
dt1 = dt.groupby('Company').describe().transpose()['GOOGLE']
print(dt1)