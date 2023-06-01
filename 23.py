import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YU_oppdivide!20",
    database="menagerie"
)

mycursor = db.cursor()

mycursor.execute("SELECT owner, COUNT(*) AS pet_count FROM pet GROUP BY owner")

print("Owner          Number of pets")
for x in mycursor:
    print(f"{x[0]:<20}{x[1]}")

mycursor.close()
db.close()
