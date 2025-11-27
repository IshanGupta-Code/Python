# Creating a Summary of the data
# Methods 
'''
df.['Column Name'].mean()
df.['Column Name'].sum()
df.['Column Name'].count()
df.['Column Name'].min()
df.['Column Name'].max()
df.['Column Name'].std()
'''

import pandas as pd

data = {
    "Name": ['ishan' , None , 'ansh' , 'prince' , 'nepali' , 'siddharth' , 'monk' , 'ayush' , 'gautam'],
    "Age" : [23, None, 56, 34, 23, 67, 52, 45, 38],
    "Salary": [23000 , None, 45000, 26000, 8900 , 120000, 23000, 34000, 45000],
    "Performance_Score": [7, None, 9, 7, 8, 9, 7, 8, 4 ]
}   

df = pd.DataFrame(data)

print('Smaple Data')
print(df)

average_mean = df['Salary'].mean()
print('Average Salary of the Employee', average_mean)
