import numpy as np
import pandas as pd
from scipy import io

#Python-SciPy数据读取的方法如下：
#SciPy.io.savemat()    SciPy.io.loadmat()
a = np.mat('1,2,3;4,5,6')
b = np.array([[1,1,1],[2,2,2]])
io.savemat('a.mat', {'matrix': a})
io.savemat('b.mat', {'matrix': b})

c = io.loadmat('a.mat')
print(c)
