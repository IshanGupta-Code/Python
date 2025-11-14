# List is used to store multiple data
# list store different types of data like int string float
# list can store duplicate value 
# create list and store your friend name
friendName= ["ivan","anshu","anjali","wani"]

# to access the data from list
# single element access listvariablename[index]
print(friendName[3])

# to print complete the list
for name in friendName :
    print(name)
 #operation on list:-
# friendName.append("Naman")
# append always add value at last
# insert will add the data based on index no
# list can store the multiple value

friendName.insert(0,"Piyush")
friendName.insert(34,"Piyush")
# to remove the data from list
friendName.remove("ivan")
# we can't remove data from list with help of index because list is a non homogeneous with remove 
# remove delete data with value based
# remove function can only remove one data
friendName.remove("Piyush")
# this only remove first piyush data not last

# to remove data using pop

# pop can remove data using index number
friendName.pop(0)
# pop remove the last data in list

# list can add value at index which is far away from last index
friendName.reverse()
# delete all list data
friendName.clear()
for name in friendName:
    print(name)

#  print specific data slicing
# print data from list in range 
friendName= ["ivan","anshu","anjali","wani"]
for name in friendName[1:3]:
    print(name)
# not include 3

friendName.append("rahul")
friendName.append("rohit")
friendName.append("kanak")  
for name in friendName[2:6]:
   print(name)

print(friendName)
# last index value -1
for name in friendName[-4:-1]:
    print(name)
for name in friendName[-4:]:
    print(name)
for name in friendName[:-1]:
    print(name)
friendName[0]="ivan sharma"
friendName.sort()

for name in friendName[:]:
    print(name)

# sorting is not possible if list have int and string value
# wap to add the 10 students name in list,remove last value
  

