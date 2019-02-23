import numpy as np
import pandas as pd

series1 = pd.Series([1, 2, 3, 4], ['London', 'HongKong', 'Lagos', 'Mumbai'])
series2 = pd.Series([1, 3, 6, 4], ['London', 'Accra', 'Lagos', 'Delhi'])
print(series1['London'])


#对于Series的算术运算都是基于index进行的，加入Pandas在两个Series里面找不到相同的index，对应位置就会返回一个空值NaN
print(series1 - series2)
print(series1 + series2)
print(series1 * series2)





