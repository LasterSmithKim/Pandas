import matplotlib.pyplot as plt
import pylab as pl
import pandas as pd
import numpy as np


df = pd.read_excel('../../data/al4-3.xls')
#将列对象放入单独的数据变量中：
t = np.array(df[['year']])
x = np.array(df[['total']])
y = np.array(df[['new']])

#输入绘图命令：
pl.plot(t, x)
pl.plot(t, y)
pl.title('Population census')
pl.xlabel('Time')
pl.ylabel('Population')
pl.show()
