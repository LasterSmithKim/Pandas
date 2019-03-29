import numpy as np
import pandas as pd
import tushare as ts
import os

filename = 'bigfile.csv'
for code in ['000875', '600848', '000981']:
    df = ts.get_hist_data(code)
    if os.path.exists(filename):
        df.to_csv(filename, mode='a', header=None)#如果不考虑header，每次都会将columns也append进去
    else:
        df.to_csv(filename)
