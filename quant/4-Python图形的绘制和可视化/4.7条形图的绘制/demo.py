import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_excel('../../data/al4-1.xls')
var = df.groupby('Gender').Sales.sum()
#grouped sum of sales at Gender level
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_xlabel('Gender')
ax1.set_ylabel('Sum of Sales')
ax1.set_title('Gender wise Sum of Sales')
var.plot(kind='bar')
plt.show()