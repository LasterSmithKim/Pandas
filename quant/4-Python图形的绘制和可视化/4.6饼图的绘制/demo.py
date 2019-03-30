import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_excel('../../data/al4-1.xls')

var = df.groupby(['Gender']).sum().stack()
temp = var.unstack()
x_list = temp['Sales']
label_list = temp.index
plt.axis('equal')
plt.pie(x_list)
plt.title('Pastafatianism expenses')
plt.show()

