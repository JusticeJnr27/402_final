# create_fill_database.py
import mysql.connector as mc

# connect to database
conn = mc.connect(
    host="localhost",
    user="root",
    password="YU_oppdivide!20",
    db="pythonSQL",
)
c = conn.cursor()  # cursor to perform operations


def create_table():
    """Create table in the database."""
    # optional: drop table if exists
    c.execute("DROP TABLE IF EXISTS writer")
    c.execute(
        "CREATE TABLE writer \
            ( \
                id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, \
                name VARCHAR(30) NOT NULL UNIQUE, \
                age int \
            )"
    )


def insert_data():
    """Insert data to the table."""
    c.execute("INSERT INTO writer (name) VALUES ('Pearl Buck')")
    c.execute(
        " INSERT INTO writer VALUES \
        (NULL, 'Rabindranath Tagore', 80), \
        (NULL, 'Leo Tolstoy', 82)"
    )
    c.execute(
        " INSERT INTO writer (age, name) VALUES \
    (30, 'Meher Krishna Patel')"
    )


def commit_close():
    """Commit changes to database and close connection."""
    conn.commit()
    c.close()
    conn.close()


def main():
    """Execute create and insert commands."""
    create_table()
    insert_data()
    commit_close()  # required for save the changes


# standard boilerplate to call main function
if __name__ == "__main__":
    main()