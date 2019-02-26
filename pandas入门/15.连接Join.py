import numpy as np
import pandas as pd

#如果两张表没有太多共同的列，可以考试使用join()方法  ，它与.merge()不同在于连接采用索引作为公共的键 而不是某一列

left = pd.DataFrame({'A': ['A0', 'A1', 'A2'], 'B': ['B0', 'B1', 'B2']}, index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'], 'D': ['D0', 'D2', 'D3']}, index=['K0', 'K2', 'K3'])

df = left.join(right)
print(df)

df = left.join(right, how='outer')
print(df)

# inner 表示交集 ；  outer 表示并集