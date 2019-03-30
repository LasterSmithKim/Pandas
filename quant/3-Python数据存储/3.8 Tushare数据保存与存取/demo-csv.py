import numpy as np
import pandas as pd
import tushare as ts

#保存为csv格式

df = ts.get_hist_data('000875')
df.to_csv('000875.csv')
df.to_csv('000875.csv', columns=['open', 'high', 'low', 'close'])



#读取csv数据文件
df1 = pd.read_csv('000875.csv')
print(df1.head())

