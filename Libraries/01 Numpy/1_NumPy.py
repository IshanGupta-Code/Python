import numpy as np

'''# assign array in numpy 

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

# Reverse the order of an array
rev = np.flip(myFriends)
print(rev)

x = 3
while x >= 0 :
    print(myFriends[x])
    x = x - 1

# Sort
print(np.sort(myData))
print(np.sort(myFriends))


# Zeros , Ones and Full
zeros = np.zeros(3)  # np.zeros(size of an array)
ones = np.ones((2,3))  #np.ones(row*coloumn)
full = np.full((2,3),7) #np.full((row*coloumn),value)
print(zeros)
print(ones)
print(full)

#Arange(start,stop,step)
arange = np.arange(1,100,2)
print(arange)

#Eye(Size)
eye = np.eye(3)
print(eye)

# Shape
print(eye.shape)
print(eye.size)
print(eye.ndim , "Dimension")
print(eye.dtype)
eye = eye.astype(int)
print(eye.dtype)

# Operations
matrix2 = np.array([10,20,30,40])
print(matrix2 + 20)
print(matrix2 * 6)
print(matrix2 ** 2)

# Aggregate function
agrregate = np.array([10,20,30,40,50,60,70])
print(np.sum(agrregate))
print(np.min(agrregate))
print(np.max(agrregate))
print(np.mean(agrregate))
print(np.std(agrregate))
print(np.var(agrregate))

# Indexing & Slicing
index = np.array([10,20,30,40,50])
print(index[0])
print(index[1])
print(index[2])
print(index[3])
print(index[4])

print(index[0:3])
print(index[::])
print(index[::2])
print(index[::-1])  # --> Reverse the array without any loops

# Fancy Indexing
print(index[[0,4,3]])

# Boolean Mastering
print("\nBoolean Mastering")
print(index[index > 25])

# Reshaping
print("\nReshaping")
reshape1 = np.array([1,2,3,4,5,6])
print("Original :", reshape1)
reshape = reshape1.reshape(2,3)
print(reshape)

# Flattering
array_2d = np.array([[1,2,3], [4,5,6]])
print(array_2d.flatten())
print(array_2d.ravel())

## Manupulation
Insert in 1D array
insert = np.array([1,2,3,4,5,6])
newinsert = np.insert(insert , 2 , 100, axis=None)
print(newinsert)

# Insert in 2D array
insert = np.array([[1,2,3,4,5,6], [1,2,3,4,5,6]])
newinsert = np.insert(insert , 1 , [1,2,3,4,5,78], axis=0)
print(newinsert)

#Append
append1 = np.array([10,20,30,40,50])
append2 = np.array([60,70,80,90,100])
final_array = np.append(append1 , [100,200,300,400,500])
print(final_array)
final_array = np.append(append1 , append2)
print(final_array)

#Concatenate
append1 = np.array([10,20,30,40,50])
append2 = np.array([60,70,80,90,100])
end_result = np.concatenate((append1, append2), axis=0)
print(end_result)

#Delete
delete = np.array([10,20,30,40,50])
deleted_array = np.delete(delete , 0)
print(deleted_array)

delete1 = np.array([[10,20,30,40,50] , [60,70,80,90,100]])
deleted_array1 = np.delete(delete1 , 0 , axis=0)
print(deleted_array1)

#Stacking
stack1 = np.array([1,2,3,4,5])
stack2 = np.array([6,7,8,9,10])
print(np.vstack((stack1 , stack2))) # Vertical Stacking
print(np.hstack((stack1 , stack2))) # Horizontal Stacking

#Spliting
split = np.array([10,20,30,40,50,60,70,80,90,100])
split1 = np.array([[1,2,3,4,5] , [6,7,8,9,10]])
print(np.split(split , 2))
print(np.vsplit(split1 , 1))
print(np.hsplit(split1 , 1))
'''
#Broadcasting 
prices = np.array([100,200,300])
discount = 10 
final_prices = prices-(prices * discount / 100)
print(final_prices)

#Handling Misisng Value
missing_value = np.array([1 , 2 , np.nan , 4 , np.nan])
print(missing_value)
print(np.isnan(missing_value))
cleaned_array = np.nan_to_num(missing_value, nan=100)
print(cleaned_array)

#Infinite
infinte_value = np.array([1 , 2 , -np.inf , 4 , np.inf])
print(infinte_value)
print(np.isinf(infinte_value))
cleaned_array = np.nan_to_num(infinte_value , posinf=5 , neginf=3)
print(cleaned_array)

# Absolute 

# Create a NumPy array
arr = np.array([-5, -3.14, 0, 2.71, 10])

# Calculate the absolute values
abs_arr = np.abs(arr)

print(abs_arr)


# numpy --> Dataset Create
#  Panda --> Dataset Represent
#  Matplotlib --> Graphically Data Display

