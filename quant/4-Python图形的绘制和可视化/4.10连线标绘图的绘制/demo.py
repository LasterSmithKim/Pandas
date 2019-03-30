import matplotlib.pyplot as plt
import pylab as pl
import pandas as pd
import numpy as np


df = pd.read_excel('../../data/al4-4.xls')
#将列对象放入单独的数据变量中：
t = np.array(df[['year']])
x = np.array(df[['number']])

#输入绘图命令：
pl.plot(t, x)
pl.title('1998-2015 of A listed companies in China')
pl.xlabel('Time')
pl.ylabel('Companies numbers')
pl.show()

pl.plot(t, x, 'ro')
pl.title('1998-2015 of A listed companies in China')
pl.xlabel('Time')
pl.ylabel('Companies numbers')
pl.show()
