import sqlite3

connection = sqlite3.connect()
cursor = connection.cursor()
def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS calcss(input TEXT, result TEXT)""")
    connection.commit()
    return

def insert_calc(expersion, result):
    cursor.execute(f"""INSERT INTO calcss VALUES({expresion},{result})""")
    connection.commit()
    return
