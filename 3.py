import mysql.connector as mc

conn = mc.connect(
    host="localhost",
    user="root",
    password="YU_oppdivide!20"
)
c = conn.cursor()
c.close()
conn.close()
