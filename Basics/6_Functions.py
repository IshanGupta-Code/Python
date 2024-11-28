'''# function can perform any task and it can reuse anytime
def printName():
    print("My function name is print")
# function calling 
printName()
# argument function and parameter function
def myAge(age):
    print("My age is :",age)

myAge(18)  

# find the area of square using function
def squareArea(value):
    area=side*side
    print("area of square is =",area)

side=int(input("enter side of square="))
squareArea(side)'''

# return keyword use
side=int(input("enter side of square="))
def areaofSquare(value):
    return value*value
output=areaofSquare(side)

print("area of square =", output)    
    