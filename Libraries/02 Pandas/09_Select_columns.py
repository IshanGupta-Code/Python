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

# Select and Print Data of Single Columns
print("Name (single columns return series)")
name = df['Name']
print(name)

# Select and Print Data of Multiple Columns
age = df[['Name' , 'Age']]
print(age)