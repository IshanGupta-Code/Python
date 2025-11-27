import numpy as np

# assign array in numpy 

myData = np.array([1,2,3,4])
print(myData)
print(type(myData))
# <class 'numpy.ndarray'>  --->> Here, .nd is N Dimensional array

# Update the data in Array
myData[0] = 9
myData[1] = 10
myData[2] = 11
myData[3] = 12
print(myData)

# By For Loop
print("By For Loop")
a = 9
for data in range(0,4):
    myData[data] = a + data
print(myData)

# By While loop
print("By While Loop")
i = 0
x = 12
while i < 4:
    myData[i] = x
    x = x - 1
    i = i + 1
print(myData)

# Access the data from numpy array
print("Print Array")
for data in range(0,4):
    print(myData[data])
# for data in myData:
#     print(data)


myFriends = np.array(["Ishan","Anshu","Vibhore","Swastik"])
for name in myFriends:
    print(name)

# Reverse the array
rev = np.flip(myFriends)
print(rev)

x = 3
while x >= 0 :
    print(myFriends[x])
    x = x - 1

# Sort
print(np.sort(myData))
print(np.sort(myFriends))



# numpy --> Dataset Create
#  Panda --> Dataset Represent
#  Matplotlib --> Graphically Data Display

