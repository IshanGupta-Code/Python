# Sorting value with condition

import pandas as pd

data = {
    "Name": ['ishan' , None , 'ansh' , 'prince' , 'nepali' , 'siddharth' , 'monk' , 'ayush' , 'gautam'],
    "Age" : [23, 45, 56, 34, 23, 67, 52, 45, 38],
    "Salary": [23000 , None, 45000, 26000, 8900 , 120000, 23000, 34000, 45000],
    "Performance_Score": [7, None, 9, 7, 8, 9, 7, 8, 4 ]
}   

df = pd.DataFrame(data)

print('Smaple Data')


# df.sort_values(by='Age', ascending=True, inplace=True)
# Multiple Columns
df.sort_values(by=['Age', 'Salary'], ascending=[True, False], inplace=True)
print('Sorted Age by Decending')
print(df) 