import numpy as np
import pandas as pd

countries = ['USA', 'Nigeria', 'France', 'CN']
my_data = [100, 200, 300, 400]

#my_series = pd.Series(data, index)
my_series = pd.Series(my_data, countries)
print(my_series)

#index可以缺省，直接输入数据
my_series1 = pd.Series(my_data)
print(my_series1)

#Creating Series from Python Dictionary
my_dict = {'a':100, 'b':200, 'c':300, 'd':400}
my_series2 = pd.Series(my_dict)
print(my_series2)


#Creating Series from a NumPy Array
np_arr = np.array(my_data)
print(np_arr)
my_series3 = pd.Series(np_arr)
print(my_series3)
















