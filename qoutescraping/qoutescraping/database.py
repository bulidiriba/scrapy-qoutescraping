import sqlite3

conn = sqlite3.connect("myquotes.db")
curr = conn.cursor()

# CREATE TABLE
# if the table is already created comment this block of code
curr.execute('''create table quotes_tb(
                title text,
                author text,
                tag text
            )''')

# INSERT THE VALUE
curr.execute('''insert into quotes_tb values ("Python is awesome!", "buildwithpython", "python")
            ''')

conn.commit()
conn.close()