# Tab Space is called indentation

# try:
#     error
# catch:
#     type of error

# print(x)
try:
    print(x)
except NameError :
    print("X Not Defined")

try:
    y = 1/0
    print(y)
except ZeroDivisionError:
    print("Zero Division Error")

try:
    a = "ishan" 
    b = int(a)
    print(b)
except ValueError:
    print("String Can't cast in Integer")

try:
    import os
    os.remove("myfile.txt")
except FileNotFoundError:
    print("File is Not Created")

try:
    mylist = ["ishan","fhihbb"]
    print(mylist[4])
except IndexError:
    print("Index not Found")

# try:
#     x = 5
#     if x > 5 :
#     print(x)
#     else :
#     print(x)
# except IndentationError :
#     print("IndentationError")

try:
    x = "ishan"
    y = 4
    c = x + y
    print(c)
except TypeError:
    print("Type Error")










