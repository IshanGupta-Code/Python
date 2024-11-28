# Class --> It is a collection of object and function.
# Object --> It is the 

# Class Name is always in CamelCase
class ishan:
    print("My name is Ishan Gupta")
    age = 18
    email = "Temp@gmail.com"

# Object Creation
# object : Class = Class
isha : ishan = ishan()
print("My name is:",isha.age)
print("My email I'D:",isha.email)

class Student:
    # Objects
    name ="ishan"
    email = "temp@gamil.com"
    # Function
    def findMyAge(this, cY,bY):  # "this" -> used to give current class reference
        ageInYear = cY - bY
        print("My age is:",ageInYear)
    def monthlyPocketMoney(this,weeklyMoney):
        pocketMoney = weeklyMoney * 4
        print("Monthly Pocket Money is:",pocketMoney)


obj:Student  = Student()
obj.findMyAge(2024,2005)
obj.monthlyPocketMoney(int(input("Weekly Money: ")))

class Car:
    model = 2024
    gear = 7
    first_gear = 50
    def topSpeed (this, gear):
        speed = 50 * gear 
        print("the top speed is:",speed)

car:Car = Car()
car.topSpeed(int(input("Enter No. of Gear (1 - 7): ")))