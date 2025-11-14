# .loc[]  --> To Location or select the specific cell in the dataset

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

# Update the value of spesific cell
# syntax : df.loc[row_index , 'column_name'] = new_value
updated_list = df.loc[0 , 'Salary'] = 43000
print('After Updating Value\n' , updated_list)

# Update the value of whole column
df['Salary'] = df['Salary'] * 1.05
print(df)