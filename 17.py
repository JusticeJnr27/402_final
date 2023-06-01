import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YU_oppdivide!20",
    database="menagerie"
)

mycursor = db.cursor()

mycursor.execute("SELECT * FROM pet WHERE species = 'dog' AND sex = 'f' ")

for x in mycursor:
    print(x)
