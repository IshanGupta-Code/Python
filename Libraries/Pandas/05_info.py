import pandas as pd

df = pd.read_csv(r"E:\Code\Python\Libraries\Pandas\sales_data_sample.csv" , encoding= "latin1")

print('Displaying the info the dataset')
print(df.info())