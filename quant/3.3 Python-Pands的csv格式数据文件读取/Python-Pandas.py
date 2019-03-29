import numpy as np
import pandas as pd

a = ['apple', 'pear', 'watch', 'money']
b = [[1,2,3,4,5], [5,7,8,9,0], [1,3,5,7,9], [2,4,6,8,0]]
d = dict(zip(a,b))

p = pd.DataFrame(d)
p.to_csv('IBM.csv')

print(pd.read_csv('IBM.csv'))