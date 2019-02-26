import numpy as np
import pandas as pd


#读取excel
df = pd.read_excel('excel_output.xlsx', sheet_name='Sheet1')
print(df)

#写入excel
data = {
            'A': ['Dog', 'Dog', 'Dog', 'Goat', 'Goat', 'Goat'],
            'B': ['Brown', 'Brown', 'Black', 'Black', 'Brown', 'Brown'],
            'C': ['x', 'y', 'x', 'y', 'x', 'y'],
            'D': [1,3,2,5,4,1]
        }
df1 = pd.DataFrame(data)
df1.to_excel('excel_input.xlsx', sheet_name='Sheet1', index=False)



