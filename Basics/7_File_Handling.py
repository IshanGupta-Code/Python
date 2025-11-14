#create file in python with name and extension
myfile=open("Ishan.txt","w")
#write name and 
myfile.write('''My name is Ishan Gupta and email id : guptaishan506@gmail.com''')
#to close the file
myfile.close()

#Read the data from file
readFile=open("Ishan.txt","r")
print(readFile.read())



# #Delete the file
# import os
# os.remove("Ishan.txt")



#Create stock api in json -> java script object notation
myStock=open("myStock.json","w")
#myStock.write("this is my stock api")    not a json data
# {} -> JsonObject  , []-> JsonArray
myStock.write('''{"name":"Ishan gupta"}''')
readStock=open("myStock.json","r")
print(readStock.read())


#read and write the data in xls, csv and json files.....