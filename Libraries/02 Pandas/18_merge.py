# Merging 2 DataFrames  (Left, Right, Inner, Outer)

import pandas as pd

Coustomer_Data = pd.DataFrame({
    'Name' : ['Ishan', 'Vibhore' , 'Ansh' , 'Gull' , 'Nepolian'],
    'Age' : [23,34,45,67,78],
    'OrderID' : [1,2,3,4,5]
})

Billing_Data = pd.DataFrame({
    'OrderID' : [1,2,4,5],
    'Amount' : [230,234,67,323]
})

Merged_data = pd.merge(Coustomer_Data , Billing_Data , on='OrderID', how='right')
print('Merged Data\n' , Merged_data)