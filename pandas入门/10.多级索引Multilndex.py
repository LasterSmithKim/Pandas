import numpy as np
import pandas as pd


outside = ['0 Level', '0 Level', '0 Level', 'A Level', 'A Level', 'A Level']
inside = [21, 22, 23, 21, 22, 23]
#list(zip())嵌套函数，将两个列表合并成一个 每个元素都是 元组的列表
#  [('0 Level', 21), ('0 Level', 22), ('0 Level', 23), ('A Level', 21), ('A Level', 22), ('A Level', 23)]
my_index = list(zip(outside,inside))


#using Multilndex.from_tuples()function,we will create a multi-level index
#MultiIndex(levels=[['0 Level', 'A Level'], [21, 22, 23]],
#           codes=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]])
my_index = pd.MultiIndex.from_tuples(my_index)



#Finally, let's convert our multi-level data into a DataFrame
df = pd.DataFrame(np.random.randn(6,2),index=my_index,columns=['A', 'B'])
#给索引添加名字
df.index.names=['Levels','Num']
print(df)
print(df.loc['0 Level'])
print(df.loc['0 Level'].loc[21])


#交叉选择行和列中的数据 可以使用 .xs() 方法
print(df.xs(22,level='Num'))


