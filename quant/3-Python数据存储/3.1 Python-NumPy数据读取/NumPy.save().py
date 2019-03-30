import numpy as np
import pandas as pd

a = np.mat('1,2,3;4,5,6')
b = np.array([[7, 8, 9], [10, 11, 12]])
np.save('a.npy', a)
np.save('b.npy', b)
