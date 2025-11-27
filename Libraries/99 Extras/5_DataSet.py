import numpy as np
import pandas as pd
import json
myData=np.arange(0,1000000)
# print(myData)
myFrame=pd.DataFrame(data=myData.reshape(1000,1000))
# print(myFrame)
# # top 10 highest paid salary
# # we need to first change combination
myfile=("5_sample.json","w")
# # we dont need import to csx
myfile=("5_sample.csv","w")
myfile=("5_sample.xlsx","w")
myFrame=pd.DataFrame(data=myData.reshape(100000,10))
myFrame.to_excel("5_sample.xlsx")
myFrame.to_csv("5_sample.csv")
myFrame.to_json("5_sample.json")
print(myFrame.tail(1))
print(myFrame.loc[[2,]])
# # this prints the third row
# # loc will return the row index value
# # iloc will return the data in combintion of row and column 
# print(myFrame.iloc[2:6,0:2]) # first is row and second one is column 
# print(myFrame.iloc[2:5,7:10])
# print(myFrame.iloc[8:10,4:6])
# #write your data from dataframe to json file
# #read data from json
# myjson=pd.read_json("5_sample.json")
# print(myjson)
# # # read data from csv
# mycsv=pd.read_csv("5_sample.csv")
# print(mycsv)
# # read data from excel
# myexcel=pd.read_excel("5_sample.xlsx")
# print(myexcel)