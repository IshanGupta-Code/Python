# dictionary can store the data in key value pair
# name:ishan 
# ordered , no duplicate , changable
myInfo={ "name":"ishan Pandey",
                    "email":"e.ishan@gmail.com",
                     "mobile":"8908768XYZ",
                     "age":18,
                     "name":"ishan"} #dictionary dont hold duplicate it automaticaaly give last same key value
# dictionary is used for storing particular or individual person details 
print(type(myInfo))    
 #  to find one information in dictionary
print("my name is ="+myInfo["name"]+" my gmail id is="+myInfo["email"]+" my mobile number is="+myInfo["mobile"]+" my age is =",myInfo["age"])
# second case
print(f"MY NAME IS {myInfo["name"]},i am {myInfo["age"]} year old and email{myInfo["email"]}and mobile no is {myInfo["mobile"]}")
# access the complete dictionary key values 
for value in myInfo.values():
    print(value)
    #for accessing keys  
for key in myInfo.keys():
    print(key)    
    #how we can aasign the values in dictionary
    # myinfo["name"]="ishan" automaticaaly update the data
myInfo["name"]="prince"
myInfo["email"]="prince@gmail.com"
myInfo["mobile"]="908765690"
myInfo["age"]= 18
# for value in myInfo.values():
#     print(value)
print(f"MY NAME IS {myInfo["name"]} i am {myInfo["age"]} year old and email{myInfo["email"]}and mobile no is {myInfo["mobile"]}")
# to add new info
myInfo.update({"gender":"male"})
print(myInfo["gender"])
# to remove one info
# variabledict_name.pop("key")
myInfo.pop("age")
print(myInfo)

