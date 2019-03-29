import numpy as np
import pandas as pd
import tushare as ts

symbols = ['600000', '000980', '000981']
data = pd.DataFrame()

data1 = ts.get_hist_data('600000',start='2018-01-01',end='2018-10-01')
data1 = data1['close']
data1 = data1[::-1]
data['600000'] = data1

data1 = ts.get_hist_data('000980',start='2018-01-01',end='2018-10-01')
data1 = data1['close']
data1 = data1[::-1]
data['000980'] = data1

data1 = ts.get_hist_data('000981',start='2018-01-01',end='2018-10-01')
data1 = data1['close']
data1 = data1[::-1]
data['000981'] = data1

#查看数据情况
print(data.info())
#清理数据
data = data.dropna()#na删除数据
print(data.info())

print(data.head())
print(data.tail())

print(data[['600000', '000981']].head())

#取2行到4行的数据
print(data[['600000', '000981']].ix[1:4])
#取第1行到第2行 及 第1列到第3列的数据
print(data[['600000', '000981']].iloc[:2,:3])

