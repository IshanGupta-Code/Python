# Grouping Data as per the given condition like(mean, min, max, etc)

import pandas as pd

data = {
    "Name": ['ishan' , 'vibhor', 'ansh' , 'prince' , 'nepali' , 'siddharth' , 'monk' , 'ayush' , 'gautam'],
    "Age" : [23, 34, 23, 34, 23, 52, 52, 45, 38],
    "Salary": [23000 , 23000, 45000, 26000, 8900 , 120000, 23000, 34000, 45000],
    "Performance_Score": [7, 10, 9, 7, 8, 9, 7, 8, 4 ]
}   

df = pd.DataFrame(data)

print('Smaple Data')
print(df)

# Single Columns
# grouped_data = df.groupby('Age')['Salary'].sum()

# Multiple Columns
grouped_data = df.groupby(['Age', 'Name'])['Salary'].sum()
print('After grouping\n' ,grouped_data)
