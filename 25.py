import mysql.connector
from tabulate import tabulate

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YU_oppdivide!20",
    database="menagerie"
)

mycursor = db.cursor()

mycursor.execute("SELECT name, birth, MONTH(birth) AS month FROM pet")

headers = ["Name", "Birth", "Month(birth)"]
rows = []
for x in mycursor:
    rows.append([x[0], x[1], x[2]])

print(tabulate(rows, headers, tablefmt="grid"))

mycursor.close()
db.close()
