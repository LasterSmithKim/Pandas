import numpy as np
import pandas as pd
import pandas_datareader.data as web
from pandas import DataFrame

data_feed = {}

data_feed[1] = web.get_data_yahoo('AAPL', '01/12/2018', '31/12/2018')
data_feed[2] = web.get_data_yahoo('FB', '01/12/2018', '31/12/2018')


price = DataFrame({tic: data['Adj Close'] for tic, data in data_feed.items()})
print(price.head())

print(price.tail())

