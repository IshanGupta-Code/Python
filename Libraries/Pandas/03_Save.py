import pandas as pd

data = {
    "Name": ['Ishan' , 'Prince' , 'Siddharth' , 'Nepali'],
    "Age": [10 , 20 , 30 , 40],
    "City": ['Nagpur' , 'Banaras' , 'Sahibabad' , 'Noida']
}

df = pd.DataFrame(data)

print(df)

# df.to_csv("output.csv" , index=False)
# df.to_excel("output.xlsx" , index=False)
df.to_json("output.json" , index=False)
