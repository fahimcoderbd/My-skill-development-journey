import sqlite3

#creating db connection
conn = sqlite3.connect('skill\\04_Advanced\\database\\sqlite3\\my_db.db')

#creating cursor for db tasks
cursor = conn.cursor()

#creating queries here
#Created MYINFO TABLE - my personal info
#cursor.execute("CREATE TABLE MYINFO (Id INTEGER, Name TEXT, Age INTEGER, City TEXT)")

#adding data to the table
#cursor.execute("INSERT INTO MYINFO VALUES(2, 'Fahim', 17, 'Rajshahi')")

#reading data from the table
cursor.execute("SELECT * FROM MYINFO")

My_info = cursor.fetchall()
for data in My_info:
    print(data)

#update operation
""" cursor.execute(
    "UPDATE MYINFO SET Name=? WHERE Id=?",
    ('Rahib', 2)
) """

#delete operation
""" cursor.execute(
    "DELETE FROM MYINFO WHERE Id=?",
    (2,)
) """

#saving db queries
conn.commit()
#closing connection
conn.close()

