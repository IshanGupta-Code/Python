# Using insert Function or Method

import pandas as pd

data = {
    "Name": ['ishan' , 'vibhore' , 'ansh' , 'prince' , 'nepali' , 'siddharth' , 'monk' , 'ayush' , 'gautam'],
    "Age" : [23, 45, 56, 34, 23, 67, 52, 45, 38],
    "Salary": [23000 , 25000, 45000, 26000, 8900 , 120000, 23000, 34000, 45000],
    "Performance_Score": [7, 8, 9, 7, 8, 9, 7, 8, 4 ]
}   

df = pd.DataFrame(data)

print('Smaple Data')
print(df)

# This Method add Column in the last position
df['Bonus'] = df['Salary'] * 0.1
print("Bonus Column Added :\n" , df)
# print(df)

# Using Insert Function
# syntax : df.inert(column_index , 'column_name' , [data])
df.insert(0 , "Employee id" , [1,2,3,4,5,6,7,8,9]) 
print('Using Insert Function\n' , df)

