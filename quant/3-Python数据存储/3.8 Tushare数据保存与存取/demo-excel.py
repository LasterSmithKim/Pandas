import numpy as np
import pandas as pd
import tushare as ts
import os

#保存excel数据
df = ts.get_hist_data('000875')
df.to_excel('000875.xls')
#df.to_excel('000875.xls', startrow=2, startcol=5)#设定数据插入位置（从第3行，第6列开始插入数据）


#读取excel数据
df1 = pd.read_excel('000875.xls')
print(df1.head())
