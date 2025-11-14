# here in pandas data set called data frame 
import numpy as np
import pandas as pd
# PANDSAS LIKE EXCEL 
import matplotlib.pyplot as pit
x=np.array([1,2,3,4])
myDataFrame=pd.DataFrame(x)
print(myDataFrame)

myData=pd.DataFrame(data=np.arange(0,100).reshape(10,10))
print(myData)
print(myData.head())
# head prints top 5 default
print(myData.tail())
# tail will find last 5 data default
# for specific
print(myData.head(7))
# suppose this data is company salary
# we have to give commision of 1000 to each
print(myData+1000)
print(myData.describe())
print(myData.mean())
print(myData.mode())
print(myData.median())
# loc function print particular data specific row
print(myData.loc[[2,3]])
print(myData.loc[[0,3]])

print(myData.loc[[9]])
print(myData.loc[[]])
print(myData.loc[[0,]])