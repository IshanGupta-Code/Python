import pandas as pd

region1 = pd.DataFrame({
    'region' : [1,2,3,4,5],
    'name' : ['ishan', 'kiran' ,'shyam', 'ram', 'haram']
})

region2 = pd.DataFrame({
    'region' : [6,7,8,9,10],
    'name' : ['ishan', 'kiran' ,'shyam', 'kallu' , 'hello']
})

combine_data = pd.concat([region1 , region2], axis=1, ignore_index=True)
print(combine_data)
