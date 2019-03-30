import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_excel('../../data/al4-1.xls')
fig = plt.figure()
ax = fig.add_subplot(111)
#Variable
ax.boxplot(df['Age'])
plt.title('Box figure of Age')
plt.show()

#绘制多属性箱型图
vars = ['Age', 'Sales']
data = df[vars]
plt.show(data.plot(kind='box'))
