import mysql.connector

# Connect to MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YU_oppdivide!20"
)

# Create a cursor object
mycursor = mydb.cursor()

mycursor.execute("show databases")

for i in mycursor:
    print(i)
