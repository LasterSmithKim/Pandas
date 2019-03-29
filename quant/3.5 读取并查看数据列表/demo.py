import numpy as np
import pandas as pd

data = pd.DataFrame(pd.read_excel('../data/al3-1.xls'))

#将Z1设为自变量X Z2设为因变量Y
X = np.array(data[['Z1']])
Y = np.array(data[['Z2']])
#查看自变量和因变量的行数
print(X.shape)

print(Y.shape)