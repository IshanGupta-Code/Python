# not used predefined keywords for class name
# for loop is used to complete iteration or repeating the task
name=input("enter your name")
# iterate my name using for loop
# e.g. in c for(int i=0;i<=10;i++)
for i in name :
    print(i)

#print the numbers upto 10
for x in range(1,11):
 # first parameter in range is starting and second is end point and end point not include
    print (x) 

 #print thsi pattern using for loop 1 3 5 7 9 11
    for x in range(1,12,2):
    #   2 is step size by default step size is 1
      print(x)
 #do with if 
for x in range(1,12):
      if  x % 2 !=0:
        print(x)

# print the even no and odd no from 1 to 20
print("odd numbers are:")
for x in range(1,21,2):
    print(x)

print("even numbers are:")
for x in range(2,21,2):  
    print(x)  

 # do this with if else condition
for x in range(1,21):
    if x%2!= 0:
        print("odd numbers are=",x)
    else:
        print("even numbers are=",x)        