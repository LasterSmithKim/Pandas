import numpy as np
import pandas as pd


df = pd.DataFrame(np.random.randn(5,4),['a', 'b', 'c', 'd', 'e'],['W', 'X', 'Y', 'Z'])

#打印'W'大于0的行数据
print(df[df['W']>0])

#  W大于0的行中  X Y 的数据
print(df[df['W']>0][['X', 'Y']])

# W 大于 0 和   X 大于 1 的行
print(df[(df['W']>0) & (df['X']>1)])
