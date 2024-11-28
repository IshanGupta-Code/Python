# How to find the data type of Variable
amount = 2500.45
print(amount) # -> to read any statement in python
print(type(amount))

# Typecasting : Convert one datatype to another datatype.

# Convert Float to Int
amount = int(amount)
print(amount)
print(type(amount))

# Convert Int to String
price = 2400
stringPrice = str(price)
print(stringPrice, " and the datatype is ", type(stringPrice))

# Convert String to Int (conversion not possible beacuse string does't have ASCII NO)
gender = "male"
# genderIntoInt = int(gender)
# print(genderIntoInt," and the datatype is ", type(genderIntoInt))

# To take the input from user c language scanf
myName = input("Enter your Name ")
myAge = input("Enter Your age ")  # input function default returntype is String
myAge = int(input("Enter Your age "))  # input function returntype is int
print("My name is "+ myName + " and Age is", myAge)

# Practice Problem (Find age in years when Bornyear given by user)

bornYear = int(input("Enter your Born Year "))
currentYear = int(input("Enter your Current Year "))
print(currentYear - bornYear ,"year")


# Practice Problem (Currency convert Program rupee to USD :- 84)

dollar = 84
rupeeQuantity = int(input("Enter the Rupee Value "))
print("The value of Dollar is: ", dollar*rupeeQuantity)

# Data type is used to  defined the data in which form 
# int data is used to store th numeric type data 
# notein python we don't need 
# we just assign the value in variable 
# Variable can store any type of value with type of data
age = 33
name = "ishan"
salary = 123.234

# how to pass the variables inside the print statement
# we have 3 ways to pass the variable in print statement 
# print ("My name is "+ name + " and salary" + salary + " and age" + age)
# it generates the Type error, reason string only concetenated with string not int
# Solution 1 :- replace + by, when data type is not string 
print("My name is "+ name + "and salary", salary , " and age ", age)

# Solution 2: pass the variable in print statement with f()
print(f"My Name is {name} salary is {salary} and age {age}")
# Solution 3: typecasting the data into string
salaryString =str(salary)
ageString = str(age)
print("My name is " + name +" and salary " + salaryString + " and age" + ageString)

# to find thr type of data we need to use type() Function
print(type(name))
print(type(age))
print(type(salary))







































#Check the user age eligible for vote and super vote 
# Super vote age should be greater than 55 
# vote age should be greater than 18 less than 55
userAge = input("Enter the Age to check eligibility")
if userAge > 18 and userAge <55 :
    print("You'r eligible for voting")
elif userAge > 55 :
    print("You are not eligible") 
else :
    print("You are Underage or Overage")