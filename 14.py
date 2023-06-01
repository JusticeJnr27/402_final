import mysql.connector as mc
from tabulate import tabulate


conn = mc.connect(host="localhost", user="root", password='YU_oppdivide!20', db="menagerie")
c = conn.cursor()


def read_data():
    c.execute("SELECT * FROM pet")
    pets = c.fetchall()
    headers = ["name", "owner", "species", "sex", "birth", "death"]
    print(tabulate(pets, headers, tablefmt="grid"))


def main():
    read_data()


if __name__ == "__main__":
    main()
