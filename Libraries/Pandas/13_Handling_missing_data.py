# Misiing Data Handling [dropna , fillna]

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

# isnull() : to indentify the missing value (it return's boolean value)
# isnull().sum() : to get the sum of missing value
print('Identify Missing Value')
print(df.isnull().sum())

# Handling of Missing Value (3 Methods [dropna , fillna , interpolate])

# dropna : for deleting the whole row(0) or columns(1) of the missing value (0 index is selected by default)
'''
# syntax : df.dropna(index = 0 , inplace = true)
df.dropna(inplace= True)
print('After removing row \n' , df)
'''

#fillna() : to fill the missing value
'''
df.fillna(0 , inplace= True) #fill missing value with single value
'''
df['Age'].fillna(df['Age'].mean() , inplace=True)
df['Salary'].fillna(df['Salary'].mean() , inplace=True)
print(df)



# There is another method written in 14 number file