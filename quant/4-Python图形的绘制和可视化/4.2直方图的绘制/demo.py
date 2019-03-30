import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_excel('../../data/al4-1.xls')

#绘制直方图命令如下：
fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(df['Age'], bins=7)
plt.show()

#给图形增加标题
fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(df['Age'], bins=7)
plt.title('Age distribution')
plt.show()

#给坐标轴增加数值标签
fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(df['Age'], bins=7)
plt.title('Age distribution')
plt.xlabel('Age')
plt.ylabel('#Employee')
plt.show()


