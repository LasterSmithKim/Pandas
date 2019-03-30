import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_excel('../../data/al4-1.xls')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(df['Age'], df['Sales'], s=df['Income'])
#Added third variable income as size of the bubble
#通过气泡图，可以看出这些雇员的年龄和收入情况，还可以根据气泡的大小看出雇员的收入情况
plt.xlabel('Age')
plt.ylabel('Sales')
plt.show()