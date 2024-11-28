# in pyhton there are very few datatypes 

# 1. int ---> integer can used to store integer value.
# 2. str ---> it used to store string value.
# 3. float ---> it can store the decimal value.

# Integer
a = 23
print(a,"--> This is an Interger Value")

# Float( Decimal Value )
b = 45.3
print(b,"--> This is an Decimal Value")

# String ( String Value )
c = "Ishan"
print(c,"--> This is an String Value")


# TO STORE MULTIPLE VALUES

# 1. List --> it can store multiple value with different datatype.
friendsName = ["rahul", "anshu", 1234] # --> it use "[]" 
print(type(friendsName))
print(friendsName[2])

# 2. Tuple -> it can store multiple values but can't be modified.
number = (1,2,"hello")  # --> it use "()"
print(type(number))
print(number[0])

# 3. Set -> is an unordered collection of unique elements
mySet = {1.2,34,56,"ishan"} # --> it use "{}"
print(type(set))
print(mySet)

# 4. Dictionary(Dict)
person = {"name": "Alice", "age": 30}
name = person["name"]
print(name)


