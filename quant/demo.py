import numpy as np
import pandas as pd
import tushare as ts
import os

df = ts.get_today_all()
print(df)