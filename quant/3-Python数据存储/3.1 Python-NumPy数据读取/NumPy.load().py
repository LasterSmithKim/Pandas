import numpy as np
import pandas as pd

data_a = np.load('a.npy')
data_b = np.load('b.npy')

print('data_a \n', data_a, '\n the type is ', type(data_a))
print('data_b \n', data_b, '\n the type is ', type(data_b))

#将 a , b 保留到同一个文件， np.savez()

np.savez('ab.npz', k_a=data_a, k_b=data_b)
c = np.load('ab.npz')
print(c['k_a'])
print(c['k_b'])