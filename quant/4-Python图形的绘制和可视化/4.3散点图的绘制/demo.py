import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_excel('../../data/al4-1.xls')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(df['Age'], df['Sales'])
#You can also add more variables here to represent color and size.
plt.title('Age and Sales Scatter of Employee')
#Variable
plt.xlabel('Age')
plt.ylabel('Sales')
plt.show()