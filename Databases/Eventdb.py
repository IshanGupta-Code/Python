import mysql.connector

# create databases connection to mysql
connection = mysql.connector.connect(host = "localhost",
                                     username = "root",
                                     password = "@Ishangupta1234",
                                     database = "event")

# to check the connection establish or not
if connection.is_connected():
    print("db is connected")
else:
    print("db not connected")

# # to create user table in database
# users = "create table if not exists users(fname text)"

# #to pass the cursor handle sql query
# mycursor = connection.cursor()

# #to execute the sql query
# mycursor.execute(users)
# connection.commit()

# # to insert fname is user table
# insertName = "insert into users values('{}')".format("ishangupta")
# mycursor.execute(insertName)
# connection.commit()

######### NEXT DAY #########


# to create user table in database
users = "create table if not exists addevent(eventname text, username text, eventdate text, email text, departure text, mobile text)"

#to pass the cursor handle sql query
mycursor = connection.cursor()

#to execute the sql query
mycursor.execute(users)
connection.commit()

# to insert fname is user table
# insertName = "insert into addevent values('{}','{}','{}','{}','{}','{}')".format(input("Enter Event Name: "), input("Enter User Name: "),input("Enter Event Date: "), input("Enter Student Email: "), input("Enter Department Name: "), input("Enter Student Mobile No.: "))
# mycursor.execute(insertName)
# connection.commit()

# to update the event details in database
updateEvent = "update addevent set eventname = 'VAM' where mobile = '0987654321'"
mycursor.execute(updateEvent)
connection.commit()

# to delete the event from database
deleteEvent = "delete from addevent where mobile = '1234567890'"
mycursor.execute(deleteEvent)
connection.commit()

# to fetch the event list from database
eventList = "select * from addevent"
mycursor.execute(eventList)
print(mycursor.fetchall())
connection.commit()

# to drop the event table
dropEvent = "drop table addevent"
mycursor.execute(dropEvent)
connection.commit()