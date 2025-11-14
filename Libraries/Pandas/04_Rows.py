# Method - head()  and  tail() defeault value is 5 

# head means - upper 5 rows
# tail means - lower 5 rows


import pandas as pd

df = pd.read_csv(r"E:\Code\Python\Libraries\Pandas\sales_data_sample.csv" , encoding= "latin1")

print('Display first 5 rows')
print(df.head())

print('\nDisplay last 5 rows')
print(df.tail())