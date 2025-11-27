# Handling Missing Data [interpolate] (only for integer values)
import pandas as pd

data = {
    "Name": ['ishan' , 'Shyam' , 'ansh' , 'prince' , 'nepali' , 'siddharth' , 'monk' , 'ayush' , 'gautam'],
    "Age" : [23, None, 56, 34, 23, 67, 52, 45, 38],
    "Salary": [23000 , None, 45000, 26000, 8900 , 120000, 23000, 34000, 45000],
    "Performance_Score": [7, None, 9, 7, 8, 9, 7, 8, 4 ]
}   

df = pd.DataFrame(data)

print('Smaple Data' , df)


# Interpolate (It uses many method like linear, time, polynomial)
df.interpolate(method= 'linear', axis=0, inplace=True)