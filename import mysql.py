import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="27898188Mw!",
  database= "menagerie"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASE menagerie")
for x in mycursor:
  print(x)
