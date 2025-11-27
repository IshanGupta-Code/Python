import pandas as pd

data = {
    "Name": ['ishan' , 'vibhore' , 'ansh' , 'prince' , 'nepali' , 'siddharth' , 'monk' , 'ayush' , 'gautam'],
    "Age" : [23, 45, 56, 34, 23, 67, 52, 45, 38],
    "Salary": [23000 , 250000, 45000, 86000, 89000 , 120000, 23000, 34000, 45000],
    "Performance_Score": [7, 8, 9, 7, 8, 9, 7, 8, 4 ]
}   

df = pd.DataFrame(data)

print('Smaple Data')
print(df)

# Printing as per the given condition
print('Salary as per given condition (> 50000)')
high_salary = df[df['Salary'] > 50000]
print(high_salary)

# Data printing multiple condition
print('Salary > 50000 and Age > 30')
filltered = df[(df['Salary'] > 50000) & (df['Age'] > 30)]  # Here we can also use "|" (pipe) for 'or' condition
print(filltered)

# Print only Salary and Age
only_data = filltered[['Salary' , 'Age']]
print(only_data)