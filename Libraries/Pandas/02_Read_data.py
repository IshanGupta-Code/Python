import pandas as pd

# Reading of the data
data_file = r"E:\Code\Python\Libraries\Pandas\sales_data_sample.csv"
df = pd.read_csv(data_file , encoding = "latin1")

print(df)