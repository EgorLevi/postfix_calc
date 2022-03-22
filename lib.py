import sqlite3

connection = sqlite3.connect("history.db")
cursor = connection.cursor()
def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS calcss(input TEXT, result TEXT)""")
    connection.commit()
    return

def insert_calc(expersion, result):
    try:
        cursor.execute(f"""INSERT INTO calcss VALUES({expersion},{result})""")
        connection.commit()
    except:
        create_table()
        insert_calc(expersion, result)
    return

insert_calc("2+2", "4")
