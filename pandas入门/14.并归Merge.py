import numpy as np
import pandas as pd


#使用 pd.merge()函数，能将多个DataFrame并归在一起，它的合并方式类似合并SQL数据表
#语法：pd.merge(left,right,how='inner',on='Key)    其中：left表示左侧的dataframe，right表示右侧的dataframe
#当左右两个表中Dataframe中存在不重合的Key时，取结果的方式： inner表示交集；outer表示并集；
#on='Key'代表需要合并的键值所在的列，最后整个表格会以该列为准进行归并。


left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'C': ['C0', 'C1', 'C2', 'C3'],
                     'D': ['D0', 'D1', 'D2', 'D3']})
pd = pd.merge(left, right, how='inner', on='key')
print(pd)


'''
#传入多个on参数，这样就可以按多个键值进行并归，类似 多键
left1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right1 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
pd1 = pd.merge(left1, right1, on=['key1', 'key2'])
print(pd1)
'''
