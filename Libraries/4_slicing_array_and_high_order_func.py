# python provides high order function like mean ,sort etc
import numpy as np # create data
import pandas as pd # represent data 
import matplotlib.pyplot as pit #in graph

x=np.array([1,7,8,11,9,3,2,4])
# print("The mean =",x.mean())
# print("The maximum =",x.max())
# print("The minimum=",x.min())
# x.sort()
# print(x)

for i in x:
    for j in x:
     if i<j:
      i=j
      print(i)
# we need to sort the data without high order function
# Arry slicing =it will get the data from inside the  array whether it can be full data or selected data
print(x[0:8])   
print(x[2:6])
print(x[2:])
print(x[:7])
print(x[3:11])
print(x[:]) #meaning zero to last index

print(x[-5:-1])
# negative indexing -1 is last index and its left side like -2 ,-3,-4....so on
# last index will be subtract to -1
print(x[-6:-2])  
print(x[:-1])
# shape and reshape 
print(x.shape)
# reshape can change large data set into small data set
# make data more readable
myData=x.reshape(2,4)
print(myData)
y=np.array([3,1,7,9,2,11,8,10])
# add two array
z=x+y
print(z)


    
    

# python provides high order function like mean ,sort etc
import numpy as np # create data
import pandas as pd # represent data 
import matplotlib.pyplot as pit #in graph

x=np.array([1,7,8,11,9,3,2,4])
# print("The mean =",x.mean())
# print("The maximum =",x.max())
# print("The minimum=",x.min())
# x.sort()
# print(x)

for i in x:
    for j in x:
     if i<j:
      i=j
      print(i)
# we need to sort the data without high order function
# Arry slicing =it will get the data from inside the  array whether it can be full data or selected data
print(x[0:8])   
print(x[2:6])
print(x[2:])
print(x[:7])
print(x[3:11])
print(x[:]) #meaning zero to last index

print(x[-5:-1])
# negative indexing -1 is last index and its left side like -2 ,-3,-4....so on
# last index will be subtract to -1
print(x[-6:-2])  
print(x[:-1])
# shape and reshape 
print(x.shape)
# reshape can change large data set into small data set
# make data more readable
myData=x.reshape(2,4)
print(myData)
y=np.array([3,1,7,9,2,11,8,10])
# add two array
z=x+y
print(z)